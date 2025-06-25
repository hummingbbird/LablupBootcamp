import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(number):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, f"https://jsonplaceholder.typicode.com/posts/{number}")
        print(response)

if __name__ == '__main__':
    asyncio.run(main(1))
