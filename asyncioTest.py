import asyncio

async def test():
    print("Test")
    return "test"

async def main_test():
    await test()

# 이것을 해주어야 main_test가 돌아가겠지요~
if __name__ == '__main__':
    asyncio.run(main_test())