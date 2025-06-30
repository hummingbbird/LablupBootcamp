# server.py
# WebSocket을 통한 실시간 채팅
# redis 연동하여 메시지 broadcast
from aiohttp import web, WSMsgType
import asyncio
from client import pubMessage, subscribe_channel
import json


connected_users = {} # 현재 연결된 클라이언트 딕셔너리

# WebSocket 접속 및 메시지 처리
async def websocket_handler(request):

    # response 응답 객체
    ws = web.WebSocketResponse()
    await ws.prepare(request) # http -> ws 연결로 전환

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
            except:
                pass

    return ws

# 새 메시지 받을 때마다 메시지 broadcast
async def redis_listener():
    async for message in subscribe_channel("chatroom"):
        # 연결된 users 모두에게
        for ws in list(connected_users.keys()):
            try:
                # 새 메시지 WebSocket으로 전송
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
