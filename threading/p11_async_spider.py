"""
    python单线程异步IO实现并发爬虫
    单线程异步一般都要比多线程还快的
"""

import time
import asyncio
import aiohttp      # 不用requests是因为他不支持异步IO


urls = [f"https://www.cnblogs.com/sitehome/p/{page}" for page in range(1, 50 + 1)]


async def async_craw(url):      # 定义一个协程
    print('craw url: ', url)
    async with aiohttp.ClientSession() as session:      # 创建对象
        async with session.get(url) as resp:
            result = await resp.text()                  # 获取结果
            print(f"craw url: {url}, {len(result)}")


def main():
    loop = asyncio.get_event_loop()                     # 定义一个超级循环
    tasks = [loop.create_task(async_craw(url)) for url in urls]      # 创建了一个tasks列表

    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))        # 等待tasks完成
    end = time.time()
    print('use time seconds: ', end - start)            # use time seconds:  0.43076229095458984


if __name__ == '__main__':
    main()