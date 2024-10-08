import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"


async def main():
    """很多个task的话写很多个await就麻烦，可以用gather"""
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    
    print(f"started at {time.strftime('%X')}")
    
    ret = await asyncio.gather(task1, task2)    # 告诉main，要等这里面每一个task都完成才能继续执行，同时把这些task的返回值放到一个list并返回
    print(ret)
    
    print(f"finished at {time.strftime('%X')}")


async def main2():
    """gather可以直接把coroutine变成task"""
    
    print(f"started at {time.strftime('%X')}")
    
    ret = await asyncio.gather(
        say_after(1, "hello"),
        say_after(2, "world")
    )
    print(ret)
    
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())