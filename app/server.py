from aiohttp import web, WSMsgType
import asyncio
from client import pubMessage, subscribe_channel
import json
import logging


connected_users = {} # user 리스트
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger('webchat')

async def websocket_handler(request):
    ws = web.WebSocketResponse() # socket response 받을 ws
    await ws.prepare(request)

    nickname = "알 수 없음" # default값 설정
    connected_users[ws] = nickname

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            try:
                data = json.loads(msg.data) # data를 json 형식으로 변환
                logger.info(f"data: {data}")
                if data["type"] == "join":
                    nickname = data["nickname"]
                    connected_users[ws] = nickname
                    print(f"connect_users: {connected_users}")
                    await pubMessage("chatroom", f"{nickname} 님이 입장했습니다.")
                elif data["type"] == "chat":
                    await pubMessage("chatroom", f"{connected_users[ws]}: {data['message']}")
                elif data["type"] == "leave":
                    await pubMessage("chatroom", f"{connected_users[ws]} 님이 방을 나갔습니다.")
            except Exception as e:
                logger.info(e)

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

web.run_app(app, host="0.0.0.0", port=8080)
