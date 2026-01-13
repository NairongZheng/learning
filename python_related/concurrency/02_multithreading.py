"""
多线程示例

两个最常见的场景：
- 模拟**批量网络请求**（I/O 密集型）
- 模拟**批量 API 调用**（I/O 密集型）
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


# ==================== 场景 1：批量网络请求（模拟） ====================
def fake_network_request(url: str, delay: float = 0.1) -> dict:
    """
    模拟网络请求：
    - 模拟网络延迟（I/O 等待）
    - 返回响应数据
    """
    time.sleep(delay)  # 模拟网络延迟（I/O 等待）
    return {
        "url": url,
        "status": 200,
        "content_length": len(url) * 100,
    }


def example_network_requests(num_requests: int, request_delay: float) -> None:
    print("=" * 50)
    print("示例 1：批量网络请求（模拟，无真实网络 IO）")
    print("=" * 50)

    urls = [f"https://api.example.com/data/{i}" for i in range(1, num_requests + 1)]

    # 单线程
    start = time.time()
    single_results = []
    for url in tqdm(urls, total=len(urls), desc="单线程请求"):
        single_results.append(fake_network_request(url, delay=request_delay))
    single_time = time.time() - start
    print(f"单线程处理 {len(urls)} 个请求耗时: {single_time:.3f} 秒")

    # 多线程（线程池）
    max_workers = min(20, len(urls))  # 线程数不超过任务数，且不超过20（避免过多线程）

    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 使用 submit 提交任务，然后用 as_completed 获取结果（支持进度条）
        futures = {executor.submit(fake_network_request, url, request_delay): url for url in urls}
        multi_results = []

        for future in tqdm(as_completed(futures), total=len(futures), desc="多线程请求",):
            multi_results.append(future.result())
    multi_time = time.time() - start
    print(f"多线程处理 {len(urls)} 个请求耗时: {multi_time:.3f} 秒")
    print(f"加速比: {single_time / multi_time:.2f}x")


# ==================== 场景 2：批量 API 调用（模拟） ====================
def fake_api_call(api_id: int, delay: float = 0.05) -> dict:
    """
    模拟 API 调用：
    - 模拟 API 响应延迟（I/O 等待）
    - 模拟数据处理
    """
    time.sleep(delay)  # 模拟 API 响应延迟
    # 模拟一些轻量级的数据处理
    result = sum(range(api_id % 100))
    return {
        "api_id": api_id,
        "result": result,
        "processed": True,
    }


def example_batch_api_calls(num_apis: int, api_delay: float) -> None:
    print("=" * 50)
    print("示例 2：批量 API 调用（模拟，无真实网络 IO）")
    print("=" * 50)

    api_ids = list(range(1, num_apis + 1))

    # 单线程
    start = time.time()
    single_results = []
    for api_id in tqdm(api_ids, total=len(api_ids), desc="单线程调用 API"):
        single_results.append(fake_api_call(api_id, delay=api_delay))
    single_time = time.time() - start
    print(f"单线程处理 {len(api_ids)} 个 API 调用耗时: {single_time:.3f} 秒")

    # 多线程（线程池）
    max_workers = min(30, len(api_ids))  # 线程数不超过任务数，且不超过30

    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(fake_api_call, api_id, api_delay): api_id
            for api_id in api_ids
        }
        multi_results = []

        for future in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="多线程调用 API",
        ):
            multi_results.append(future.result())
    multi_time = time.time() - start
    print(f"多线程处理 {len(api_ids)} 个 API 调用耗时: {multi_time:.3f} 秒")
    print(f"加速比: {single_time / multi_time:.2f}x")


def main():
    print("\n" + "=" * 50)
    print("Python 多线程编程示例")
    print("适用于 I/O 密集型任务")
    print("=" * 50 + "\n")

    # 计算规模设置
    num_requests = 100  # 网络请求数量
    request_delay = 0.1  # 每个请求的延迟（秒），越大 I/O 等待越长，多线程优势越明显
    num_apis = 200  # API 调用数量
    api_delay = 0.05  # 每个 API 调用的延迟（秒）

    example_network_requests(num_requests=num_requests, request_delay=request_delay)
    example_batch_api_calls(num_apis=num_apis, api_delay=api_delay)

    print("=" * 50)
    print("示例运行完成")
    print("=" * 50)


if __name__ == "__main__":
    main()
