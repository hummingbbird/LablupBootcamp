# client.py
# Redis와 비동기 통신 위한 파일(Pub/Sub 함수 구현)
# server에서 Redis로 publish, subscribe할 때 import 해서 사용함
import redis.asyncio as redis
import os


REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

# Redis 비동기 클라이언트
client = redis.Redis(
    host=REDIS_HOST,
    port=6379,
    decode_responses=True
)

# 메시지 원하는 채널로 전송(publish)
async def pubMessage(channel, message):
    await client.publish(channel, message)

# 원하는 채널 구독 및 메시지 수신(yield)
async def subscribe_channel(channel):
    pubsub = client.pubsub()
    await pubsub.subscribe(channel) # 비동기적으로 subscribe
    async for msg in pubsub.listen(): # 새 메시지 도착히 yield
        if msg["type"] == "message":
            print("Redis 수신:", msg["data"])
            yield msg["data"]
