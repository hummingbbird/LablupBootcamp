import asyncio
import time

# async def test():
#     time.sleep(2)
#     print("test1")
#     return 

# async def main_test():
#     await test()
#     print("test2")

# # 이것을 해주어야 main_test가 돌아가겠지요~
# if __name__ == '__main__':
#     asyncio.run(main_test())

async def test(n):
    print(f"test{n} 실행시작")
    await asyncio.sleep(n)
    print(f"test{n} 실행 완")
    return 

async def main_test():
    start = time.time()
    await asyncio.gather(asyncio.create_task(test(5)), asyncio.create_task(test(1)))
    end = time.time()
    print(f"총 소요 시간: {end-start}")

# 이것을 해주어야 main_test가 돌아가겠지요~
if __name__ == '__main__':
    # main_test()
    asyncio.run(main_test())