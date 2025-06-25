# windows의 경우 redis.msi 설치해주어야 redis가 잘 돌아감
# import redis
# import redis.exceptions

# try:
#     r = redis.Redis(host="localhost", port=6379, db=0)
#     r.set('hello', 'world') # key value 값으로 입력
# except redis.exceptions.ConnectionError as e:
#     print(f"실패:{e}")

# print(r.get('hello'))

import redis.asyncio as redis
import asyncio

async def main():
    redis_conn = redis.Redis(host="localhost", port=6379, db=0)
    print(await redis_conn.ping())
    await redis_conn.set("maru", "dog")
    print(await redis_conn.get("maru"))

    await redis_conn.aclose()

asyncio.run(main())