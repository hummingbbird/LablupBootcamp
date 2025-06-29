# server.py
# WebSocket을 통한 실시간 채팅
# redis 연동하여 메시지 broadcast
from aiohttp import web, WSMsgType
import asyncio
from client import pubMessage, subscribe_channel
import json


connected_users = {} # 현재 연결된 클라이언트 리스트

# WebSocket 접속 및 메시지 처리
async def websocket_handler(request):
    # response 응답 객체
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    nickname = "알 수 없음"
    connected_users[ws] = nickname

    # 클라이언트로부터 받은 메시지 처리
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            try:
                data = json.loads(msg.data) # json 파싱

                # type 별 메시지 publish
                if data["type"] == "join":
                    nickname = data["nickname"]
                    connected_users[ws] = nickname
                    await pubMessage("chatroom", f"---[{nickname} 님이 입장했습니다.]---")
                elif data["type"] == "chat":
                    await pubMessage("chatroom", f"{connected_users[ws]}: {data['message']}")
                elif data["type"] == "leave":
                    await pubMessage("chatroom", f"--- [{connected_users[ws]} 님이 방을 나갔습니다.]---")
            except Exception as e:
                print(f"error: {e}")

    return ws

async def redis_listener():
    async for message in subscribe_channel("chatroom"):
        for ws in list(connected_users.keys()):
            try:
                await ws.send_str(message)
            except:
                pass

# index.html 연결
async def index(request):
    return web.FileResponse('./static/index.html')

# redis 실행
async def on_startup(app):
    app['redis_task'] = asyncio.create_task(redis_listener())

# 라우터 및 서버 실행
app = web.Application()
app.router.add_get("/", index)
app.router.add_get("/ws", websocket_handler)
app.router.add_static("/static/", path="./static", name="static")
app.on_startup.append(on_startup)  

web.run_app(app, host="0.0.0.0", port=8080)
