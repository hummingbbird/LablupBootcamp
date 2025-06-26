import redis.asyncio as redis
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
)
logger = logging.getLogger('redis-client')

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
# REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
logger.info(f"redis host, port: {REDIS_HOST}")

client = redis.Redis(
    host=REDIS_HOST,
    port=6379,
    decode_responses=True
)

# 메시지 전송
async def pubMessage(channel, message):
    await client.publish(channel, message)

# 채널 접속
async def subscribe_channel(channel):
    pubsub = client.pubsub()
    await pubsub.subscribe(channel)
    print(f"pubsub.listen(): {pubsub.listen()}")
    async for msg in pubsub.listen():
        if msg["type"] == "message":
            print("Redis 수신:", msg["data"])
            yield msg["data"]
