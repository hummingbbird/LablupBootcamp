from aiohttp import web, WSMsgType
import asyncio
from redis_client import publish_message, subscribe_channel
import json

connected_users = {}  # WebSocket: 닉네임 매핑

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    nickname = "알 수 없음"
    connected_users[ws] = nickname

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            try:
                data = json.loads(msg.data)
                # print("웹소켓 메시지 도착:", msg.data)
                if data["type"] == "join":
                    nickname = data["nickname"]
                    connected_users[ws] = nickname
                    await publish_message("chatroom", f"🟢 {nickname} 님이 입장했습니다.")
                elif data["type"] == "chat":
                    await publish_message("chatroom", f"{connected_users[ws]}: {data['message']}")
                elif data["type"] == "leave":
                    await publish_message("chatroom", f"🔴 {connected_users[ws]} 님이 퇴장했습니다.")
            except Exception as e:
                print("메시지 처리 오류:", e)

    return ws

async def redis_listener():
    async for message in subscribe_channel("chatroom"):
        for ws in list(connected_users.keys()):
            try:
                await ws.send_str(message)
            except:
                pass

async def index(request):
    return web.FileResponse('./static/index.html')

async def on_startup(app):
    app['redis_task'] = asyncio.create_task(redis_listener())

app = web.Application()
app.router.add_get("/", index)
app.router.add_get("/ws", websocket_handler)
app.router.add_static("/static/", path="./static", name="static")
app.on_startup.append(on_startup)  

web.run_app(app, port=8080)
