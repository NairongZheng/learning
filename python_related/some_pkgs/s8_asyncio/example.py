import asyncio
import aiohttp
import requests
import time

# 目标URL列表（这里用 httpbin 测试服务，你可以替换为真实接口）
URLS = ["https://httpbin.org/get?i={}".format(i) for i in range(1, 51)]


# ================== 同步版本 ==================
def fetch_sync(url):
    """同步请求"""
    try:
        response = requests.get(url, timeout=10)
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


def run_sync():
    start = time.time()
    results = []
    for url in URLS:
        result = fetch_sync(url)
        results.append(result)
    end = time.time()
    print(f"[同步版] 共请求 {len(results)} 个接口，用时 {end - start:.2f} 秒")
    for r in results[:3]:
        print(r)


# ================== 异步版本 ==================
async def fetch_async(session, url):
    """异步请求"""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                # 尝试解析 JSON
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


async def run_async():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in URLS:
            task = asyncio.create_task(fetch_async(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
    end = time.time()
    print(f"[异步版] 共请求 {len(results)} 个接口，用时 {end - start:.2f} 秒")
    for r in results[:3]:
        print(r)


# ================== 主函数 ==================
def main():
    print("\n=== 开始异步请求 ===")
    asyncio.run(run_async())
    print("=== 开始同步请求 ===")
    run_sync()


if __name__ == "__main__":
    main()
