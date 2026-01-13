"""
多协程（异步）示例 - 高并发I/O密集型任务

适用场景：
- 大量并发I/O操作（1000+连接）
- 网络服务、爬虫、API调用
- 单线程异步，不受GIL限制

示例任务：
1. 异步HTTP请求
2. 异步文件操作
3. 异步数据库查询（模拟）
"""

import asyncio
import time
import json
from typing import List


# ==================== 基础异步函数 ====================
async def async_task(task_id, duration=1):
    """
    基础异步任务
    """
    print(f"任务 {task_id} 开始...")
    await asyncio.sleep(duration)  # 异步等待，不阻塞其他任务
    print(f"任务 {task_id} 完成！")
    return f"Result from task {task_id}"


async def fetch_url(url, delay=0.3):
    """
    模拟异步HTTP请求
    """
    print(f"开始请求: {url}")
    await asyncio.sleep(delay)  # 模拟网络延迟
    content = f"Content from {url} (length: {len(url) * 100})"
    print(f"完成请求: {url}")
    return content


async def read_file_async(filepath):
    """
    模拟异步文件读取
    在实际应用中，可以使用 aiofiles 库
    """
    print(f"读取文件: {filepath}")
    await asyncio.sleep(0.1)  # 模拟I/O延迟
    
    # 模拟文件内容
    data = {
        'filepath': filepath,
        'content': f'Data from {filepath}',
        'size': len(filepath) * 50
    }
    
    print(f"完成读取: {filepath}")
    return data


async def query_database(query_id):
    """
    模拟异步数据库查询
    """
    print(f"执行查询 {query_id}...")
    await asyncio.sleep(0.2)  # 模拟数据库查询延迟
    result = {
        'query_id': query_id,
        'data': f'Result set for query {query_id}',
        'rows': query_id * 10
    }
    return result


# ==================== 示例1：基本的协程使用 ====================
async def example1_basic_coroutine():
    """
    基本的协程使用
    """
    print("=" * 50)
    print("示例1：基本的协程使用")
    print("=" * 50)
    
    # 顺序执行（不是并发）
    start = time.time()
    result1 = await async_task(1, 0.5)
    result2 = await async_task(2, 0.5)
    result3 = await async_task(3, 0.5)
    sequential_time = time.time() - start
    print(f"顺序执行耗时: {sequential_time:.3f}秒\n")
    
    # 并发执行
    start = time.time()
    results = await asyncio.gather(
        async_task(4, 0.5),
        async_task(5, 0.5),
        async_task(6, 0.5)
    )
    concurrent_time = time.time() - start
    print(f"并发执行耗时: {concurrent_time:.3f}秒")
    print(f"加速比: {sequential_time / concurrent_time:.2f}x")
    print()


# ==================== 示例2：并发HTTP请求 ====================
async def example2_concurrent_requests():
    """
    并发HTTP请求 - 爬虫场景
    """
    print("=" * 50)
    print("示例2：并发HTTP请求（模拟爬虫）")
    print("=" * 50)
    
    urls = [f"https://example.com/page{i}" for i in range(1, 11)]
    
    # 顺序请求
    start = time.time()
    results_seq = []
    for url in urls:
        result = await fetch_url(url, 0.3)
        results_seq.append(result)
    sequential_time = time.time() - start
    print(f"\n顺序请求 {len(urls)} 个URL: {sequential_time:.3f}秒\n")
    
    # 并发请求
    start = time.time()
    tasks = [fetch_url(url, 0.3) for url in urls]
    results_concurrent = await asyncio.gather(*tasks)
    concurrent_time = time.time() - start
    print(f"\n并发请求 {len(urls)} 个URL: {concurrent_time:.3f}秒")
    print(f"加速比: {sequential_time / concurrent_time:.2f}x")
    print()


# ==================== 示例3：控制并发数量 ====================
async def example3_controlled_concurrency():
    """
    控制并发数量 - 使用信号量
    避免同时发起过多请求
    """
    print("=" * 50)
    print("示例3：控制并发数量（信号量）")
    print("=" * 50)
    
    # 创建信号量，限制同时最多5个并发
    semaphore = asyncio.Semaphore(5)
    
    async def fetch_with_semaphore(url):
        async with semaphore:  # 获取信号量
            return await fetch_url(url, 0.2)
    
    urls = [f"https://api.example.com/data{i}" for i in range(1, 21)]
    
    print(f"请求 {len(urls)} 个URL，限制并发数为 5\n")
    
    start = time.time()
    tasks = [fetch_with_semaphore(url) for url in urls]
    results = await asyncio.gather(*tasks)
    elapsed = time.time() - start
    
    print(f"\n完成 {len(results)} 个请求，耗时: {elapsed:.3f}秒")
    print(f"平均每个请求: {elapsed/len(results):.3f}秒")
    print()


# ==================== 示例4：实际应用 - 批量文件处理 ====================
async def example4_batch_file_processing():
    """
    实际应用：批量异步读取和处理文件
    """
    print("=" * 50)
    print("示例4：批量异步文件处理")
    print("=" * 50)
    
    file_paths = [f"/data/file_{i}.json" for i in range(1, 31)]
    
    print(f"需要处理 {len(file_paths)} 个文件\n")
    
    # 顺序处理
    start = time.time()
    results_seq = []
    for filepath in file_paths:
        result = await read_file_async(filepath)
        results_seq.append(result)
    sequential_time = time.time() - start
    print(f"\n顺序处理: {sequential_time:.3f}秒\n")
    
    # 并发处理
    start = time.time()
    tasks = [read_file_async(filepath) for filepath in file_paths]
    results_concurrent = await asyncio.gather(*tasks)
    concurrent_time = time.time() - start
    print(f"\n并发处理: {concurrent_time:.3f}秒")
    print(f"加速比: {sequential_time / concurrent_time:.2f}x")
    
    # 显示部分结果
    print("\n处理结果示例：")
    for result in results_concurrent[:3]:
        print(f"  {result}")
    print()


# ==================== 示例5：异步生产者-消费者 ====================
async def example5_async_producer_consumer():
    """
    异步生产者-消费者模式
    """
    print("=" * 50)
    print("示例5：异步生产者-消费者模式")
    print("=" * 50)
    
    queue = asyncio.Queue(maxsize=10)
    
    async def producer(queue, n_items):
        """异步生产者"""
        for i in range(n_items):
            item = f"item_{i}"
            await queue.put(item)
            print(f"生产: {item}")
            await asyncio.sleep(0.1)
        print("生产者完成")
    
    async def consumer(queue, consumer_id):
        """异步消费者"""
        while True:
            try:
                item = await asyncio.wait_for(queue.get(), timeout=2.0)
                print(f"  消费者{consumer_id} 处理: {item}")
                await asyncio.sleep(0.15)  # 模拟处理
                queue.task_done()
            except asyncio.TimeoutError:
                break
    
    # 创建任务
    producer_task = asyncio.create_task(producer(queue, 20))
    consumer_tasks = [
        asyncio.create_task(consumer(queue, i))
        for i in range(3)
    ]
    
    # 等待生产者完成
    await producer_task
    
    # 等待队列清空
    await queue.join()
    
    # 取消消费者任务
    for task in consumer_tasks:
        task.cancel()
    
    print("\n所有任务处理完成")
    print()


# ==================== 示例6：异常处理 ====================
async def task_with_error(task_id, should_fail=False):
    """
    可能出错的异步任务
    """
    await asyncio.sleep(0.1)
    if should_fail:
        raise ValueError(f"任务 {task_id} 失败")
    return f"任务 {task_id} 成功"


async def example6_error_handling():
    """
    异步任务的异常处理
    """
    print("=" * 50)
    print("示例6：异常处理")
    print("=" * 50)
    
    # 方式1：使用 gather 的 return_exceptions 参数
    print("方式1：使用 gather 的 return_exceptions")
    tasks = [
        task_with_error(1, False),
        task_with_error(2, True),
        task_with_error(3, False),
        task_with_error(4, True),
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"  任务 {i}: 错误 - {result}")
        else:
            print(f"  任务 {i}: {result}")
    
    print("\n方式2：单独处理每个任务")
    tasks = [
        task_with_error(5, False),
        task_with_error(6, True),
        task_with_error(7, False),
    ]
    
    for task in asyncio.as_completed(tasks):
        try:
            result = await task
            print(f"  成功: {result}")
        except Exception as e:
            print(f"  失败: {e}")
    
    print()


# ==================== 示例7：超时控制 ====================
async def slow_task(task_id, duration):
    """
    慢速任务
    """
    print(f"任务 {task_id} 开始（需要 {duration}秒）...")
    await asyncio.sleep(duration)
    return f"任务 {task_id} 完成"


async def example7_timeout_control():
    """
    超时控制
    """
    print("=" * 50)
    print("示例7：超时控制")
    print("=" * 50)
    
    tasks = [
        slow_task(1, 0.5),
        slow_task(2, 2.0),
        slow_task(3, 0.8),
    ]
    
    print("设置超时时间为 1 秒\n")
    
    for i, task in enumerate(tasks, 1):
        try:
            result = await asyncio.wait_for(task, timeout=1.0)
            print(f"  {result}")
        except asyncio.TimeoutError:
            print(f"  任务 {i} 超时")
    
    print()


# ==================== 最佳实践建议 ====================
async def show_best_practices():
    """
    显示协程使用的最佳实践
    """
    print("=" * 50)
    print("协程（asyncio）最佳实践")
    print("=" * 50)
    print("""
1. 何时使用协程：
   - 大量并发I/O操作（1000+）
   - 网络密集型应用（爬虫、API服务）
   - 单线程就能处理的高并发场景

2. 核心概念：
   - async def: 定义协程函数
   - await: 等待异步操作完成
   - asyncio.gather(): 并发执行多个协程
   - asyncio.create_task(): 创建任务

3. 常用模式：
   - 使用 Semaphore 控制并发数
   - 使用 Queue 实现生产者-消费者
   - 使用 wait_for() 设置超时
   - 使用 as_completed() 处理先完成的任务

4. 注意事项：
   - 不要在协程中使用阻塞操作（如 time.sleep）
   - 使用异步库（aiohttp, aiofiles等）
   - CPU密集型任务不适合用协程
   - 异步代码需要在事件循环中运行

5. 性能优势：
   - 内存开销小（相比线程/进程）
   - 上下文切换快
   - 可支持成千上万的并发连接
""")


# ==================== 主函数 ====================
async def main():
    """
    主函数：运行所有示例
    """
    print("\n" + "=" * 50)
    print("Python 协程（asyncio）编程示例")
    print("适用于高并发 I/O 密集型任务")
    print("=" * 50 + "\n")
    
    # 运行各个示例
    await example1_basic_coroutine()
    await example2_concurrent_requests()
    await example3_controlled_concurrency()
    await example4_batch_file_processing()
    await example5_async_producer_consumer()
    await example6_error_handling()
    await example7_timeout_control()
    await show_best_practices()
    
    print("=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)


if __name__ == '__main__':
    # Python 3.7+ 可以直接使用 asyncio.run()
    asyncio.run(main())
