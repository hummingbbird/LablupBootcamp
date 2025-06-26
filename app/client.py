import redis.asyncio as redis

client = redis.Redis(
    host="localhost",
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
