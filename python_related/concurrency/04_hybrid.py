"""
混合并发示例

两个最常见的混合场景：
- 进程池 + 线程池：适合 CPU + I/O 混合任务
- 进程池 + 协程：适合高并发 I/O 任务
"""

import asyncio
import math
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from multiprocessing import cpu_count
from tqdm import tqdm


# ==================== 场景 1：进程池 + 线程池（CPU + I/O 混合） ====================
def io_and_cpu_task(file_id: int, io_delay: float = 0.1, compute_size: int = 50000) -> dict:
    """
    模拟混合任务：I/O（读取文件）+ CPU（复杂计算）
    """
    # 模拟 I/O 操作（文件读取）
    time.sleep(io_delay)
    
    # 模拟 CPU 密集型计算
    result = sum(math.sqrt(i) for i in range(compute_size))
    
    return {
        "file_id": file_id,
        "result": result,
        "processed": True,
    }


def process_batch_with_threads(batch_id: int, file_ids: list, io_delay: float, compute_size: int) -> list:
    """
    在单个进程中使用线程池处理一批文件
    """
    # 在这个进程中，使用线程池并发处理 I/O + CPU 任务
    with ThreadPoolExecutor(max_workers=min(10, len(file_ids))) as executor:
        tasks = [
            executor.submit(io_and_cpu_task, file_id, io_delay, compute_size)
            for file_id in file_ids
        ]
        results = [future.result() for future in tasks]
    
    return results


def example_process_plus_thread(num_files: int, batch_size: int, io_delay: float, compute_size: int) -> None:
    print("=" * 50)
    print("示例 1：进程池 + 线程池（CPU + I/O 混合）")
    print("=" * 50)

    # 将文件分批
    file_ids = list(range(1, num_files + 1))
    batches = [
        file_ids[i : i + batch_size] for i in range(0, len(file_ids), batch_size)
    ]

    print(f"总文件数: {num_files}")
    print(f"分为 {len(batches)} 批，每批约 {batch_size} 个文件")
    print(f"使用 {cpu_count()} 个进程，每个进程内使用线程池\n")

    # 单进程单线程（基准）
    start = time.time()
    baseline_results = []
    for file_id in tqdm(file_ids[:10], desc="基准（单进程单线程）"):
        result = io_and_cpu_task(file_id, io_delay, compute_size)
        baseline_results.append(result)
    baseline_time = time.time() - start
    print(f"基准耗时: {baseline_time:.3f} 秒（处理 10 个文件）\n")

    # 混合模式：进程池 + 线程池
    start = time.time()
    n_processes = min(cpu_count(), len(batches))
    n_processes = max(1, n_processes)  # 至少1个进程

    with ProcessPoolExecutor(max_workers=n_processes) as executor:
        futures = {
            executor.submit(
                process_batch_with_threads, i, batch, io_delay, compute_size
            ): i
            for i, batch in enumerate(batches)
        }
        all_results = []

        for future in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="混合模式（进程池+线程池）",
        ):
            batch_results = future.result()
            all_results.extend(batch_results)

    hybrid_time = time.time() - start
    print(f"混合模式耗时: {hybrid_time:.3f} 秒（处理 {len(all_results)} 个文件）")
    print(f"估算加速比: {(baseline_time * (num_files / 10)) / hybrid_time:.2f}x")


# ==================== 场景 2：进程池 + 协程（高并发 I/O） ====================
async def async_io_task(task_id: int, delay: float = 0.1) -> dict:
    """
    模拟异步 I/O 任务（API 调用、数据库查询等）
    """
    await asyncio.sleep(delay)  # 模拟 I/O 等待
    return {
        "task_id": task_id,
        "status": "completed",
        "result": f"Task {task_id} done",
    }


def process_with_coroutines(worker_id: int, task_ids: list, delay: float) -> int:
    """
    在单个进程中使用协程处理大量 I/O 任务
    """
    async def run_async_tasks():
        tasks = [async_io_task(task_id, delay) for task_id in task_ids]
        results = await asyncio.gather(*tasks)
        return len(results)

    # 在进程中运行协程
    count = asyncio.run(run_async_tasks())
    return count


def example_process_plus_coroutine(
    num_tasks: int, tasks_per_worker: int, io_delay: float
) -> None:
    print("=" * 50)
    print("示例 2：进程池 + 协程（高并发 I/O）")
    print("=" * 50)

    # 将任务分配给多个 worker
    task_ids = list(range(1, num_tasks + 1))
    worker_batches = [
        task_ids[i : i + tasks_per_worker]
        for i in range(0, len(task_ids), tasks_per_worker)
    ]

    print(f"总任务数: {num_tasks}")
    print(f"分为 {len(worker_batches)} 个 worker，每个 worker 约 {tasks_per_worker} 个任务")
    print(f"使用 {cpu_count()} 个进程，每个进程内使用协程\n")

    # 顺序执行（基准）
    start = time.time()
    sequential_results = []
    for task_id in tqdm(task_ids[:20], desc="基准（顺序执行）"):
        # 模拟顺序执行（在协程中顺序等待）
        async def sequential_task():
            await async_io_task(task_id, io_delay)

        asyncio.run(sequential_task())
        sequential_results.append(task_id)
    sequential_time = time.time() - start
    print(f"基准耗时: {sequential_time:.3f} 秒（处理 20 个任务）\n")

    # 混合模式：进程池 + 协程
    start = time.time()
    n_workers = min(cpu_count(), len(worker_batches))
    n_workers = max(1, n_workers)  # 至少1个进程

    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        futures = {
            executor.submit(
                process_with_coroutines, i, batch, io_delay
            ): i
            for i, batch in enumerate(worker_batches)
        }
        total_processed = 0

        for future in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="混合模式（进程池+协程）",
        ):
            count = future.result()
            total_processed += count

    hybrid_time = time.time() - start
    print(f"混合模式耗时: {hybrid_time:.3f} 秒（处理 {total_processed} 个任务）")
    print(f"估算加速比: {(sequential_time * (num_tasks / 20)) / hybrid_time:.2f}x")


def main():
    print("\n" + "=" * 50)
    print("Python 混合并发编程示例")
    print("组合使用多种并发方式")
    print("=" * 50 + "\n")

    # 计算规模设置
    # 场景1：进程池 + 线程池
    num_files = 40  # 文件总数
    batch_size = 10  # 每批文件数
    io_delay = 0.1  # I/O 延迟（秒）
    compute_size = 50000  # CPU 计算规模

    # 场景2：进程池 + 协程
    num_tasks = 200  # 总任务数
    tasks_per_worker = 50  # 每个 worker 处理的任务数
    io_delay_async = 0.05  # I/O 延迟（秒）

    example_process_plus_thread(
        num_files=num_files,
        batch_size=batch_size,
        io_delay=io_delay,
        compute_size=compute_size,
    )
    example_process_plus_coroutine(
        num_tasks=num_tasks,
        tasks_per_worker=tasks_per_worker,
        io_delay=io_delay_async,
    )

    print("=" * 50)
    print("示例运行完成")
    print("=" * 50)


if __name__ == "__main__":
    main()
