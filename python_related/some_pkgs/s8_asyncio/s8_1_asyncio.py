import asyncio

async def main():   # coroutine function (async def都是)
    print("Hello")
    await asyncio.sleep(1)  # 模拟I/O操作
    print("World")

coro = main()           # coroutine object
asyncio.run(coro)       # event loop建立之后就会去找哪个task可以执行
