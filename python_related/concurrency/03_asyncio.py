"""
多协程（异步）示例

两个最常见的场景：
- 模拟**批量网络请求**（I/O 密集型，高并发）
- 模拟**批量 API 调用**（I/O 密集型，高并发）
"""

import asyncio
import time
from tqdm import tqdm


# ==================== 场景 1：批量网络请求（模拟） ====================
async def fake_network_request(url: str, delay: float = 0.1) -> dict:
    """
    模拟异步网络请求：
    - 模拟网络延迟（I/O 等待）
    - 返回响应数据
    """
    await asyncio.sleep(delay)  # 异步等待，不阻塞其他任务
    return {
        "url": url,
        "status": 200,
        "content_length": len(url) * 100,
    }


async def example_network_requests(num_requests: int, request_delay: float) -> None:
    print("=" * 50)
    print("示例 1：批量网络请求（模拟，无真实网络 IO）")
    print("=" * 50)

    urls = [f"https://api.example.com/data/{i}" for i in range(1, num_requests + 1)]

    # 顺序执行（不是并发）
    start = time.time()
    sequential_results = []
    for url in tqdm(urls, desc="顺序请求"):
        result = await fake_network_request(url, delay=request_delay)
        sequential_results.append(result)
    sequential_time = time.time() - start
    print(f"顺序处理 {len(urls)} 个请求耗时: {sequential_time:.3f} 秒")

    # 并发执行（协程）
    start = time.time()
    tasks = [fake_network_request(url, delay=request_delay) for url in urls]
    concurrent_results = []
    
    # 使用 asyncio.as_completed 配合 tqdm 显示进度
    for coro in tqdm(asyncio.as_completed(tasks), desc="并发请求", total=len(tasks)):
        result = await coro
        concurrent_results.append(result)
    
    concurrent_time = time.time() - start
    print(f"并发处理 {len(urls)} 个请求耗时: {concurrent_time:.3f} 秒")
    print(f"加速比: {sequential_time / concurrent_time:.2f}x")


# ==================== 场景 2：批量 API 调用（模拟） ====================
async def fake_api_call(api_id: int, delay: float = 0.05) -> dict:
    """
    模拟异步 API 调用：
    - 模拟 API 响应延迟（I/O 等待）
    - 模拟数据处理
    """
    await asyncio.sleep(delay)  # 异步等待
    # 模拟一些轻量级的数据处理
    result = sum(range(api_id % 100))
    return {
        "api_id": api_id,
        "result": result,
        "processed": True,
    }


async def example_batch_api_calls(num_apis: int, api_delay: float) -> None:
    print("=" * 50)
    print("示例 2：批量 API 调用（模拟，无真实网络 IO）")
    print("=" * 50)

    api_ids = list(range(1, num_apis + 1))

    # 顺序执行
    start = time.time()
    sequential_results = []
    for api_id in tqdm(api_ids, desc="顺序调用 API"):
        result = await fake_api_call(api_id, delay=api_delay)
        sequential_results.append(result)
    sequential_time = time.time() - start
    print(f"顺序处理 {len(api_ids)} 个 API 调用耗时: {sequential_time:.3f} 秒")

    # 并发执行（协程）
    start = time.time()
    tasks = [fake_api_call(api_id, delay=api_delay) for api_id in api_ids]
    concurrent_results = []
    
    # 使用 asyncio.as_completed 配合 tqdm 显示进度
    for coro in tqdm(asyncio.as_completed(tasks), desc="并发调用 API", total=len(tasks)):
        result = await coro
        concurrent_results.append(result)
    
    concurrent_time = time.time() - start
    print(f"并发处理 {len(api_ids)} 个 API 调用耗时: {concurrent_time:.3f} 秒")
    print(f"加速比: {sequential_time / concurrent_time:.2f}x")


async def main():
    print("\n" + "=" * 50)
    print("Python 协程（asyncio）编程示例")
    print("适用于高并发 I/O 密集型任务")
    print("=" * 50 + "\n")

    # 计算规模设置
    num_requests = 200  # 网络请求数量（协程可以轻松处理大量并发）
    request_delay = 0.1  # 每个请求的延迟（秒），越大 I/O 等待越长，协程优势越明显
    num_apis = 500  # API 调用数量（协程可以处理更多并发）
    api_delay = 0.05  # 每个 API 调用的延迟（秒）

    await example_network_requests(num_requests=num_requests, request_delay=request_delay)
    await example_batch_api_calls(num_apis=num_apis, api_delay=api_delay)

    print("=" * 50)
    print("示例运行完成")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
