import redis.asyncio as redis

redis_client = redis.Redis(
    host="localhost",  # or 127.0.0.1
    port=6379,
    decode_responses=True
)

async def publish_message(channel, message):
    await redis_client.publish(channel, message)

async def subscribe_channel(channel):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel)

    async for msg in pubsub.listen():
        if msg["type"] == "message":
            print("Redis 수신:", msg["data"])
            yield msg["data"]
