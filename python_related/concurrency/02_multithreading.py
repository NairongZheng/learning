"""
多线程示例 - I/O密集型任务

适用场景：
- I/O密集型任务（网络请求、文件读写、数据库查询）
- 中等并发需求（几十到几百个任务）
- 编程简单直观

示例任务：
1. 文件读写操作
2. 网络请求（模拟）
3. 多个URL下载
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import json
import os
from pathlib import Path


# 全局计数器和锁（用于演示线程同步）
counter = 0
counter_lock = Lock()


def simulate_io_task(task_id, duration=0.5):
    """
    模拟I/O操作（如网络请求、文件读写）
    """
    print(f"任务 {task_id} 开始执行...")
    time.sleep(duration)  # 模拟I/O等待
    print(f"任务 {task_id} 完成！")
    return f"Task {task_id} result"


def download_url(url):
    """
    模拟下载URL内容
    """
    print(f"开始下载: {url}")
    time.sleep(0.3)  # 模拟网络延迟
    content = f"Content from {url}"
    print(f"完成下载: {url}")
    return content


def read_and_process_file(filepath):
    """
    读取文件并处理（模拟I/O操作）
    """
    try:
        # 模拟文件读取
        time.sleep(0.1)
        
        # 模拟处理
        result = {
            'file': filepath,
            'processed': True,
            'size': len(filepath) * 100
        }
        
        return result
    except Exception as e:
        return {'file': filepath, 'error': str(e)}


def increment_counter():
    """
    线程安全的计数器增加（演示锁的使用）
    """
    global counter
    with counter_lock:  # 使用锁保护共享资源
        current = counter
        time.sleep(0.001)  # 模拟一些操作
        counter = current + 1


# ==================== 示例1：基本的多线程使用 ====================
def example1_basic_threading():
    """
    基本的多线程使用 - 使用Thread类
    """
    print("=" * 50)
    print("示例1：基本的多线程使用")
    print("=" * 50)
    
    # 单线程
    start = time.time()
    simulate_io_task(1, 0.5)
    simulate_io_task(2, 0.5)
    simulate_io_task(3, 0.5)
    single_time = time.time() - start
    print(f"单线程总耗时: {single_time:.3f}秒\n")
    
    # 多线程
    start = time.time()
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=simulate_io_task, args=(i, 0.5))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()  # 等待所有线程完成
    
    multi_time = time.time() - start
    print(f"多线程总耗时: {multi_time:.3f}秒")
    print(f"加速比: {single_time / multi_time:.2f}x")
    print()


# ==================== 示例2：使用线程池（推荐） ====================
def example2_thread_pool():
    """
    使用线程池 - ThreadPoolExecutor（推荐方式）
    自动管理线程，避免创建过多线程
    """
    print("=" * 50)
    print("示例2：使用线程池处理多个任务")
    print("=" * 50)
    
    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
        "https://example.com/page4",
        "https://example.com/page5",
    ]
    
    # 单线程处理
    start = time.time()
    results_single = []
    for url in urls:
        result = download_url(url)
        results_single.append(result)
    single_time = time.time() - start
    print(f"\n单线程下载 {len(urls)} 个URL: {single_time:.3f}秒\n")
    
    # 线程池处理
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results_multi = list(executor.map(download_url, urls))
    multi_time = time.time() - start
    print(f"\n线程池下载 {len(urls)} 个URL: {multi_time:.3f}秒")
    print(f"加速比: {single_time / multi_time:.2f}x")
    print()


# ==================== 示例3：使用 submit 和 Future ====================
def example3_submit_future():
    """
    使用 submit 提交任务，返回 Future 对象
    可以灵活处理任务结果
    """
    print("=" * 50)
    print("示例3：使用 submit 和 Future")
    print("=" * 50)
    
    tasks = [(i, 0.2) for i in range(1, 6)]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # 提交任务，返回Future对象
        futures = {
            executor.submit(simulate_io_task, task_id, duration): task_id
            for task_id, duration in tasks
        }
        
        print("\n等待任务完成...\n")
        
        # as_completed: 哪个任务先完成就先处理哪个
        for future in as_completed(futures):
            task_id = futures[future]
            try:
                result = future.result()
                print(f"获取到结果: {result}")
            except Exception as e:
                print(f"任务 {task_id} 出错: {e}")
    
    print()


# ==================== 示例4：实际应用 - 批量文件处理 ====================
def example4_file_processing():
    """
    实际应用：批量读取和处理文件
    模拟从文件列表中读取、解析JSON、处理数据的场景
    """
    print("=" * 50)
    print("示例4：批量文件处理")
    print("=" * 50)
    
    # 模拟文件路径列表
    file_paths = [
        f"/data/file_{i}.json" for i in range(1, 21)
    ]
    
    print(f"需要处理 {len(file_paths)} 个文件\n")
    
    # 单线程处理
    start = time.time()
    results_single = []
    for filepath in file_paths:
        result = read_and_process_file(filepath)
        results_single.append(result)
    single_time = time.time() - start
    print(f"单线程处理: {single_time:.3f}秒")
    
    # 多线程处理
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results_multi = list(executor.map(read_and_process_file, file_paths))
    multi_time = time.time() - start
    print(f"多线程处理: {multi_time:.3f}秒")
    print(f"加速比: {single_time / multi_time:.2f}x")
    
    # 显示部分结果
    print("\n处理结果示例：")
    for result in results_multi[:3]:
        print(f"  {result}")
    print()


# ==================== 示例5：线程同步 - 使用锁 ====================
def example5_thread_synchronization():
    """
    线程同步：使用锁避免竞态条件
    """
    print("=" * 50)
    print("示例5：线程同步 - 使用锁")
    print("=" * 50)
    
    global counter
    
    # 不使用锁的情况（可能出错）
    counter = 0
    threads = []
    print("不使用锁的情况：")
    
    def increment_without_lock():
        global counter
        current = counter
        time.sleep(0.001)
        counter = current + 1
    
    for _ in range(10):
        t = threading.Thread(target=increment_without_lock)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"  预期结果: 10, 实际结果: {counter}")
    print(f"  {'✓ 正确' if counter == 10 else '✗ 错误（发生竞态条件）'}\n")
    
    # 使用锁的情况
    counter = 0
    threads = []
    print("使用锁的情况：")
    
    for _ in range(10):
        t = threading.Thread(target=increment_counter)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"  预期结果: 10, 实际结果: {counter}")
    print(f"  {'✓ 正确' if counter == 10 else '✗ 错误'}")
    print()


# ==================== 示例6：生产者-消费者模式 ====================
def example6_producer_consumer():
    """
    生产者-消费者模式
    使用队列进行线程间通信
    """
    print("=" * 50)
    print("示例6：生产者-消费者模式")
    print("=" * 50)
    
    from queue import Queue
    
    task_queue = Queue(maxsize=5)
    results = []
    results_lock = Lock()
    
    def producer(queue, n_items):
        """生产者：生成任务"""
        for i in range(n_items):
            item = f"item_{i}"
            queue.put(item)
            print(f"生产: {item}")
            time.sleep(0.1)
        print("生产者完成")
    
    def consumer(queue, consumer_id):
        """消费者：处理任务"""
        while True:
            try:
                item = queue.get(timeout=1)
                print(f"  消费者{consumer_id} 处理: {item}")
                time.sleep(0.2)  # 模拟处理
                
                with results_lock:
                    results.append((consumer_id, item))
                
                queue.task_done()
            except:
                break
    
    # 启动生产者
    producer_thread = threading.Thread(target=producer, args=(task_queue, 10))
    producer_thread.start()
    
    # 启动多个消费者
    consumers = []
    for i in range(3):
        t = threading.Thread(target=consumer, args=(task_queue, i))
        t.start()
        consumers.append(t)
    
    # 等待生产者完成
    producer_thread.join()
    
    # 等待队列清空
    task_queue.join()
    
    print(f"\n处理完成，共处理 {len(results)} 个任务")
    print()


# ==================== 最佳实践建议 ====================
def show_best_practices():
    """
    显示多线程使用的最佳实践
    """
    print("=" * 50)
    print("多线程最佳实践")
    print("=" * 50)
    print("""
1. 何时使用多线程：
   - I/O密集型任务（网络、文件、数据库）
   - 中等并发需求（几十到几百个任务）
   - 需要共享内存数据

2. 推荐使用线程池（ThreadPoolExecutor）：
   - 自动管理线程生命周期
   - 避免创建过多线程
   - 线程数通常设置为 I/O 操作数的 2-5 倍

3. 线程安全：
   - 使用 Lock 保护共享资源
   - 使用 Queue 进行线程间通信
   - 避免使用全局变量

4. 注意事项：
   - CPU密集型任务不适合多线程（受GIL限制）
   - 过多线程会增加上下文切换开销
   - 注意死锁问题

5. 当前活跃线程数: {}
""".format(threading.active_count()))


def main():
    """
    主函数：运行所有示例
    """
    print("\n" + "=" * 50)
    print("Python 多线程编程示例")
    print("适用于 I/O 密集型任务")
    print("=" * 50 + "\n")
    
    # 运行各个示例
    example1_basic_threading()
    example2_thread_pool()
    example3_submit_future()
    example4_file_processing()
    example5_thread_synchronization()
    example6_producer_consumer()
    show_best_practices()
    
    print("=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)


if __name__ == '__main__':
    main()
