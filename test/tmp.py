import redis.asyncio as redis
import aiohttp
import asyncio
import json

async def get(session, url):
    async with session.get(url) as response:
        return await response.text()

async def post(session, chatContent):
    return 

async def main():
    redis_conn = redis.Redis(host="localhost", port=6379, db=0)
    # 전송 버튼 클릭 시
    async with aiohttp.ClientSession() as session:
        response = await post(session, f"")
