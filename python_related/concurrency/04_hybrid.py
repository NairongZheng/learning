"""
混合并发示例 - 组合多种并发方式

适用场景：
- 复杂的应用场景，需要同时处理CPU密集和I/O密集任务
- 需要充分利用系统资源
- 大型应用架构

示例任务：
1. 进程池 + 线程池：每个进程内使用多线程
2. 进程池 + 协程：每个进程内使用协程
3. 实际应用：文件批处理（读取文件 + 复杂计算）
"""

import asyncio
import time
import json
import math
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from multiprocessing import cpu_count
from typing import List


# ==================== 辅助函数 ====================
def cpu_intensive_task(n):
    """
    CPU密集型任务：计算
    """
    result = 0
    for i in range(n):
        result += math.sqrt(i)
    return result


def io_intensive_task(task_id, duration=0.2):
    """
    I/O密集型任务：模拟文件读取
    """
    time.sleep(duration)
    return f"I/O task {task_id} completed"


async def async_io_task(task_id, duration=0.2):
    """
    异步I/O任务
    """
    await asyncio.sleep(duration)
    return f"Async I/O task {task_id} completed"


# ==================== 示例1：进程池 + 线程池 ====================
def process_with_threads(process_id, n_threads=5):
    """
    在进程中使用线程池处理I/O任务
    """
    print(f"进程 {process_id} 启动，使用 {n_threads} 个线程")
    
    # 在这个进程中，使用线程池处理I/O任务
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        tasks = [(process_id, i) for i in range(n_threads)]
        results = list(executor.map(
            lambda x: io_intensive_task(f"P{x[0]}-T{x[1]}", 0.3),
            tasks
        ))
    
    print(f"进程 {process_id} 完成")
    return f"Process {process_id}: {len(results)} tasks completed"


def example1_process_plus_thread():
    """
    示例1：进程池 + 线程池
    适用场景：多个独立任务，每个任务内部有多个I/O操作
    """
    print("=" * 50)
    print("示例1：进程池 + 线程池")
    print("=" * 50)
    print("场景：多个独立的任务组，每组内有多个I/O操作\n")
    
    n_processes = 4
    
    start = time.time()
    
    with ProcessPoolExecutor(max_workers=n_processes) as executor:
        futures = [
            executor.submit(process_with_threads, i, 5)
            for i in range(n_processes)
        ]
        
        results = [future.result() for future in futures]
    
    elapsed = time.time() - start
    
    print(f"\n完成时间: {elapsed:.3f}秒")
    print(f"总任务数: {n_processes} 个进程 × 5 个线程 = {n_processes * 5} 个任务")
    print("\n结果：")
    for result in results:
        print(f"  {result}")
    print()


# ==================== 示例2：进程池 + 协程 ====================
def process_with_coroutines(process_id, n_tasks=10):
    """
    在进程中使用协程处理大量I/O任务
    """
    print(f"进程 {process_id} 启动，处理 {n_tasks} 个协程任务")
    
    async def run_async_tasks():
        tasks = [async_io_task(f"P{process_id}-C{i}", 0.2) for i in range(n_tasks)]
        results = await asyncio.gather(*tasks)
        return results
    
    # 在进程中运行协程
    results = asyncio.run(run_async_tasks())
    
    print(f"进程 {process_id} 完成")
    return f"Process {process_id}: {len(results)} async tasks completed"


def example2_process_plus_coroutine():
    """
    示例2：进程池 + 协程
    适用场景：需要多进程隔离，但每个进程需要处理大量I/O
    """
    print("=" * 50)
    print("示例2：进程池 + 协程")
    print("=" * 50)
    print("场景：多个独立进程，每个进程内有大量并发I/O操作\n")
    
    n_processes = 3
    
    start = time.time()
    
    with ProcessPoolExecutor(max_workers=n_processes) as executor:
        futures = [
            executor.submit(process_with_coroutines, i, 15)
            for i in range(n_processes)
        ]
        
        results = [future.result() for future in futures]
    
    elapsed = time.time() - start
    
    print(f"\n完成时间: {elapsed:.3f}秒")
    print(f"总任务数: {n_processes} 个进程 × 15 个协程 = {n_processes * 15} 个任务")
    print("\n结果：")
    for result in results:
        print(f"  {result}")
    print()


# ==================== 示例3：实际应用 - 文件批处理 ====================
def read_and_process_file(filepath):
    """
    读取文件并进行CPU密集型处理
    """
    # 模拟读取文件（I/O操作）
    time.sleep(0.1)
    data = {"file": filepath, "numbers": list(range(100000))}
    
    # CPU密集型处理
    result = sum(math.sqrt(x) for x in data["numbers"])
    
    return {
        "file": filepath,
        "result": result,
        "count": len(data["numbers"])
    }


def process_file_batch(file_batch):
    """
    使用线程池处理一批文件（在单个进程中）
    """
    batch_id = file_batch[0].split('_')[1].split('/')[0]
    print(f"  批次 {batch_id} 开始处理...")
    
    # 使用线程池并发读取文件
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(read_and_process_file, file_batch))
    
    print(f"  批次 {batch_id} 完成")
    return results


def example3_file_processing_pipeline():
    """
    示例3：文件批处理流水线
    场景：大量文件需要读取（I/O）+ 复杂计算（CPU）
    
    策略：
    1. 将文件分批
    2. 使用进程池处理不同批次（利用多核处理CPU任务）
    3. 每个进程内使用线程池并发读取文件（加速I/O）
    """
    print("=" * 50)
    print("示例3：文件批处理流水线")
    print("=" * 50)
    print("场景：大量文件需要读取并进行复杂计算\n")
    
    # 生成文件列表
    all_files = [f"/data/batch_{i//10}/file_{i}.json" for i in range(40)]
    
    # 分批：每批10个文件
    batch_size = 10
    file_batches = [
        all_files[i:i+batch_size]
        for i in range(0, len(all_files), batch_size)
    ]
    
    print(f"总文件数: {len(all_files)}")
    print(f"分为 {len(file_batches)} 批，每批 {batch_size} 个文件")
    print(f"使用 {cpu_count()} 个进程处理\n")
    
    # 方式1：单进程单线程（基准）
    start = time.time()
    results_baseline = []
    for filepath in all_files[:10]:  # 只测试10个文件
        result = read_and_process_file(filepath)
        results_baseline.append(result)
    baseline_time = time.time() - start
    print(f"基准（单进程单线程处理10个文件）: {baseline_time:.3f}秒\n")
    
    # 方式2：混合模式（进程池 + 线程池）
    start = time.time()
    
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        # 每个进程处理一批文件，进程内使用线程池
        batch_results = list(executor.map(process_file_batch, file_batches))
    
    # 展平结果
    all_results = [result for batch in batch_results for result in batch]
    
    hybrid_time = time.time() - start
    
    print(f"\n混合模式完成时间: {hybrid_time:.3f}秒")
    print(f"估算的加速比: {(baseline_time * 4) / hybrid_time:.2f}x")
    print(f"处理文件总数: {len(all_results)}")
    
    # 显示部分结果
    print("\n处理结果示例：")
    for result in all_results[:3]:
        print(f"  {result['file']}: 计算结果={result['result']:.2f}, 数据量={result['count']}")
    print()


# ==================== 示例4：Web服务器模式 ====================
async def handle_request(request_id):
    """
    处理Web请求（模拟）
    包含I/O操作（数据库查询、API调用等）
    """
    # 模拟数据库查询
    await asyncio.sleep(0.1)
    
    # 模拟业务逻辑
    await asyncio.sleep(0.05)
    
    return f"Response for request {request_id}"


def run_async_server(worker_id, n_requests):
    """
    在一个worker进程中运行异步服务器
    """
    print(f"Worker {worker_id} 启动")
    
    async def handle_all_requests():
        tasks = [handle_request(f"W{worker_id}-R{i}") for i in range(n_requests)]
        results = await asyncio.gather(*tasks)
        return results
    
    results = asyncio.run(handle_all_requests())
    print(f"Worker {worker_id} 完成")
    return len(results)


def example4_web_server_pattern():
    """
    示例4：Web服务器模式
    
    架构：
    - 多个worker进程（利用多核，隔离故障）
    - 每个worker使用协程处理大量并发请求
    
    类似于：gunicorn + asyncio, uvicorn workers等
    """
    print("=" * 50)
    print("示例4：Web服务器模式")
    print("=" * 50)
    print("架构：多进程 Worker + 协程处理请求\n")
    
    n_workers = 4
    requests_per_worker = 50
    
    print(f"启动 {n_workers} 个 worker 进程")
    print(f"每个 worker 处理 {requests_per_worker} 个请求")
    print(f"总请求数: {n_workers * requests_per_worker}\n")
    
    start = time.time()
    
    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        futures = [
            executor.submit(run_async_server, i, requests_per_worker)
            for i in range(n_workers)
        ]
        
        results = [future.result() for future in futures]
    
    elapsed = time.time() - start
    
    print(f"\n完成时间: {elapsed:.3f}秒")
    print(f"总处理请求数: {sum(results)}")
    print(f"吞吐量: {sum(results) / elapsed:.2f} 请求/秒")
    print()


# ==================== 示例5：决策流程示例 ====================
def example5_decision_making():
    """
    示例5：如何选择合适的并发策略
    """
    print("=" * 50)
    print("示例5：并发策略选择指南")
    print("=" * 50)
    
    scenarios = [
        {
            "name": "图像批处理",
            "cpu_intensive": True,
            "io_intensive": False,
            "concurrency_level": "中",
            "recommendation": "多进程（ProcessPoolExecutor）",
            "reason": "CPU密集型，需要绕过GIL，利用多核"
        },
        {
            "name": "网络爬虫",
            "cpu_intensive": False,
            "io_intensive": True,
            "concurrency_level": "高（1000+）",
            "recommendation": "协程（asyncio + aiohttp）",
            "reason": "I/O密集型，大量并发，协程内存占用小"
        },
        {
            "name": "文件批量读取",
            "cpu_intensive": False,
            "io_intensive": True,
            "concurrency_level": "中（100-500）",
            "recommendation": "多线程（ThreadPoolExecutor）",
            "reason": "I/O密集型，中等并发，编程简单"
        },
        {
            "name": "文件读取+复杂计算",
            "cpu_intensive": True,
            "io_intensive": True,
            "concurrency_level": "高",
            "recommendation": "进程池 + 线程池",
            "reason": "混合任务，进程处理CPU，线程处理I/O"
        },
        {
            "name": "Web API服务器",
            "cpu_intensive": False,
            "io_intensive": True,
            "concurrency_level": "极高（10000+）",
            "recommendation": "多进程 + 协程",
            "reason": "多进程隔离故障，协程处理高并发"
        },
        {
            "name": "数据ETL流水线",
            "cpu_intensive": True,
            "io_intensive": True,
            "concurrency_level": "高",
            "recommendation": "进程池 + 线程池/协程",
            "reason": "提取(I/O)、转换(CPU)、加载(I/O)混合"
        }
    ]
    
    print("\n场景分析：\n")
    for i, scenario in enumerate(scenarios, 1):
        print(f"{i}. {scenario['name']}")
        print(f"   CPU密集: {'是' if scenario['cpu_intensive'] else '否'}, "
              f"I/O密集: {'是' if scenario['io_intensive'] else '否'}, "
              f"并发量: {scenario['concurrency_level']}")
        print(f"   推荐方案: {scenario['recommendation']}")
        print(f"   原因: {scenario['reason']}")
        print()


# ==================== 最佳实践 ====================
def show_best_practices():
    """
    混合并发的最佳实践
    """
    print("=" * 50)
    print("混合并发最佳实践")
    print("=" * 50)
    print("""
1. 选择策略原则：
   - 纯CPU密集：多进程
   - 纯I/O密集（低并发）：多线程
   - 纯I/O密集（高并发）：协程
   - CPU + I/O混合：组合使用

2. 常见组合模式：
   - 进程池 + 线程池：适合批处理，中等并发
   - 进程池 + 协程：适合高并发I/O + 进程隔离
   - 线程池 + 协程：较少使用，通常直接用协程

3. 架构设计建议：
   - 按任务类型分层处理
   - 合理控制并发数量
   - 考虑资源限制（内存、连接数）
   - 使用监控了解瓶颈

4. 性能优化：
   - 先profile找瓶颈
   - 避免过度并发
   - 注意进程/线程创建开销
   - 使用池化技术

5. 注意事项：
   - 进程间通信有开销
   - 数据序列化成本
   - 线程安全问题
   - 异步代码的调试难度
""")


# ==================== 主函数 ====================
def main():
    """
    主函数：运行所有示例
    """
    print("\n" + "=" * 50)
    print("Python 混合并发编程示例")
    print("组合使用多种并发方式")
    print("=" * 50 + "\n")
    
    # 运行各个示例
    example1_process_plus_thread()
    example2_process_plus_coroutine()
    example3_file_processing_pipeline()
    example4_web_server_pattern()
    example5_decision_making()
    show_best_practices()
    
    print("=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)


if __name__ == '__main__':
    main()
