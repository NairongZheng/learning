import asyncio
import aiohttp
import requests
import time
import aiofiles
import json
import os
from tqdm.asyncio import tqdm

# 目标URL列表（这里用 httpbin 测试服务，你可以替换为真实接口）
URLS = ["https://httpbin.org/get?i={}".format(i) for i in range(1, 51)]


class AsyncClient:
    def __init__(self, file_path="async_results.json"):
        self.file_path = file_path
        self.file_lock = asyncio.Lock()
        self.results_buffer = []
    
    async def load_results_async(self):
        """异步加载文件（带锁）"""
        async with self.file_lock:
            if not os.path.exists(self.file_path):
                return []
            async with aiofiles.open(self.file_path, "r", encoding="utf-8") as f:
                content = await f.read()
                return json.loads(content) if content else []

    async def save_results_async(self, results):
        """异步保存文件（带锁）"""
        async with self.file_lock:
            async with aiofiles.open(self.file_path, "w", encoding="utf-8") as f:
                await asyncio.sleep(0.1)  # 模拟写入耗时，放大竞争
                await f.write(json.dumps(results, ensure_ascii=False, indent=2))
    
    async def append_results(self, new_results):
        """
        异步追加文件内容（带锁）
        读写必须在同一个锁里，不然锁就形同虚设了
        上面的load跟save确实在同一个锁里，但是调用之后锁就释放了，所以还是会有问题，只能多写这个append来模拟测试
        """
        async with self.file_lock:
            if not os.path.exists(self.file_path):
                results = []
            else:
                async with aiofiles.open(self.file_path, "r", encoding="utf-8") as f:
                    content = await f.read()
                    results = json.loads(content) if content else []
            results.extend(new_results)
            async with aiofiles.open(self.file_path, "w", encoding="utf-8") as f:
                await f.write(json.dumps(results, ensure_ascii=False, indent=2))
    
    async def append_results_no_lock(self, new_results):
        """
        异步追加文件内容（不带锁，不推荐，测试用的）
        """
        if not os.path.exists(self.file_path):
            results = []
        else:
            async with aiofiles.open(self.file_path, "r", encoding="utf-8") as f:
                content = await f.read()
                results = json.loads(content) if content else []
        results.extend(new_results)
        async with aiofiles.open(self.file_path, "w", encoding="utf-8") as f:
            await f.write(json.dumps(results, ensure_ascii=False, indent=2))

    async def fetch_async(self, session, url):
        """异步请求"""
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    try:
                        data = await response.json()
                    except aiohttp.ContentTypeError:
                        text = await response.text()
                        return {"url": url, "error": "非JSON返回", "content": text[:100]}
                    return {"url": url, "args": data.get("args")}
                else:
                    return {"url": url, "error": f"HTTP {response.status}"}
        except Exception as e:
            return {"url": url, "error": str(e)}
    
    async def run_async(self):
        start = time.time()
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in URLS:
                task = asyncio.create_task(self.fetch_async(session, url))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
        end = time.time()
        print(f"[异步版] 共请求 {len(results)} 个接口，用时 {end - start:.2f} 秒")
        for r in results[:3]:
            print(r)
        # 异步写入文件
        await self.save_results_async(results)
        print(f"[异步版] 已保存结果到 {self.file_path}")
    
    async def run_async_new(self, async_num: int = 30):
        """
        使用semaphore控制并发数，使用tqdm显示进度条
        使用as_completed就绪即写，减少总体等待
        """
        start = time.time()
        semaphore = asyncio.Semaphore(async_num)
        tasks = []

        async with aiohttp.ClientSession() as session:
            async def fetch_with_semaphore(url):
                async with semaphore:
                    return await self.fetch_async(session, url)

            for url in URLS:
                task = asyncio.create_task(fetch_with_semaphore(url))
                tasks.append(task)

            pbar = tqdm(total=len(tasks), desc="异步请求处理中", unit="条")

            for coro in asyncio.as_completed(tasks):
                try:
                    result = await coro
                except Exception as e:
                    result = {"url": "unknown", "error": str(e)}

                # 用内存列表append模拟保存，并打印当前累计条数
                self.results_buffer.append(result)
                print(f"[模拟保存] 当前条数: {len(self.results_buffer)}")

                pbar.update(1)

            pbar.close()

        end = time.time()
        print(f"[异步版] 共请求 {len(self.results_buffer)} 个接口，用时 {end - start:.2f} 秒")
        for r in self.results_buffer[:3]:
            print(r)


class SyncClient:
    def __init__(self, file_path="sync_results.json"):
        self.session = requests.Session()
        self.file_path = file_path
        self.results_buffer = []
    
    def save_results_sync(self, results):
        """同步写入文件"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    
    def fetch_sync(self, url):
        """同步请求"""
        try:
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                try:
                    data = response.json()
                    return {"url": url, "args": data.get("args")}
                except ValueError:
                    # 解析 JSON 失败（返回的可能是 HTML）
                    return {"url": url, "error": "非JSON返回", "content": response.text[:100]}
            else:
                return {"url": url, "error": f"HTTP {response.status_code}"}
        except Exception as e:
            return {"url": url, "error": str(e)}
    
    def run_sync(self):
        start = time.time()
        results = []
        for url in URLS:
            result = self.fetch_sync(url)
            results.append(result)
        end = time.time()
        print(f"[同步版] 共请求 {len(results)} 个接口，用时 {end - start:.2f} 秒")
        for r in results[:3]:
            print(r)
        # self.save_results_sync(results)
        # print(f"[同步版] 已保存结果到 {self.file_path}")
        # 内存模拟保存
        self.results_buffer.extend(results)
        print(f"[同步版-模拟保存] 当前条数: {len(self.results_buffer)}")
        print(f"[同步版] 已模拟保存（未写入文件）")
    
    def close(self):
        self.session.close()


async def test_if_lock():
    client = AsyncClient("test_no_lock.json")
    async def fake_task(i):
        # 模拟不同任务得到不同的结果
        results = [{"task": i, "data": list(range(i, i + 3))}]

        # # 1. 加锁，结果不会乱
        # await client.append_results(results)

        # # 2. 加锁，但是先load再save，虽然是同一把锁，但是函数调用结束之后锁就释放了，还是会有问题的
        # old_results = await client.load_results_async()
        # old_results.extend(results)
        # await client.save_results_async(old_results)

        # 3. 不加锁，结果会乱
        await client.append_results_no_lock(results)

        return f"任务 {i} 写入完成"

    # 同时启动多个任务，几乎同时写文件
    tasks = [asyncio.create_task(fake_task(i)) for i in range(5)]
    return_values = await asyncio.gather(*tasks)
    print(return_values)
    print("所有任务完成")


# ================== 主函数 ==================
def main():
    print("\n=== 开始异步请求 ===")
    async_client = AsyncClient()
    # asyncio.run(async_client.run_async())
    asyncio.run(async_client.run_async_new())

    print("\n=== 开始同步请求 ===")
    sync_client = SyncClient()
    try:
        sync_client.run_sync()
    finally:
        sync_client.close()
    
    # print("\n=== 开始测试有无锁写入 ===")
    # asyncio.run(test_if_lock())


if __name__ == "__main__":
    main()
