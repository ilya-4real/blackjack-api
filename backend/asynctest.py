import asyncio
import time

async def foo1(a):
    print(a+2)
    await asyncio.sleep(3)
    print('foo1 ended')


async def foo2(a):
    print(a*2)
    await asyncio.sleep(3)
    print('foo2 ended')


async def main():
    task1 = asyncio.create_task(foo1(3))
    task2 = asyncio.create_task(foo2(3))

    await task1
    await task2


start = time.time()

asyncio.run(main())

print(time.time()-start)
