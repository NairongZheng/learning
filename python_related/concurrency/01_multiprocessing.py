"""
多进程示例 - CPU密集型任务

适用场景：
- CPU密集型计算（数学运算、加密、图像处理等）
- 需要绕过GIL限制
- 充分利用多核CPU

示例任务：
1. 素数判断（CPU密集型）
2. 图像处理模拟（CPU密集型）
"""

import time
import math
from multiprocessing import Process, Pool, cpu_count


def is_prime(n):
    """
    判断是否为素数（CPU密集型计算）
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    """
    找出范围内所有素数
    """
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes


def process_image_task(image_id, size=1000):
    """
    模拟图像处理任务（CPU密集型）
    对一个矩阵进行复杂运算
    """
    # 模拟图像数据
    result = 0
    for i in range(size):
        for j in range(size):
            result += math.sqrt(i * j + 1)
    
    return f"Image {image_id} processed, result: {result:.2f}"


# ==================== 示例1：基本的多进程使用 ====================
def example1_basic_multiprocessing():
    """
    基本的多进程使用 - 使用Process类
    """
    print("=" * 50)
    print("示例1：基本的多进程使用")
    print("=" * 50)
    
    # 单进程
    start = time.time()
    result1 = find_primes_in_range(10000, 10100)
    result2 = find_primes_in_range(10100, 10200)
    single_time = time.time() - start
    print(f"单进程耗时: {single_time:.3f}秒")
    
    # 多进程
    start = time.time()
    p1 = Process(target=find_primes_in_range, args=(10000, 10100))
    p2 = Process(target=find_primes_in_range, args=(10100, 10200))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    multi_time = time.time() - start
    print(f"多进程耗时: {multi_time:.3f}秒")
    print(f"加速比: {single_time / multi_time:.2f}x")
    print()


# ==================== 示例2：使用进程池（推荐） ====================
def example2_process_pool():
    """
    使用进程池 - Pool（推荐方式）
    自动管理进程数量，避免创建过多进程
    """
    print("=" * 50)
    print("示例2：使用进程池处理大量任务")
    print("=" * 50)
    
    # 准备任务：判断100个大数是否为素数
    numbers = [112272535095293] * 20  # 一个大素数，重复20次
    
    # 单进程处理
    start = time.time()
    results_single = [is_prime(n) for n in numbers]
    single_time = time.time() - start
    print(f"单进程处理 {len(numbers)} 个大数: {single_time:.3f}秒")
    
    # 多进程池处理
    start = time.time()
    with Pool(processes=cpu_count()) as pool:
        results_multi = pool.map(is_prime, numbers)
    multi_time = time.time() - start
    print(f"多进程处理 {len(numbers)} 个大数: {multi_time:.3f}秒")
    print(f"使用 {cpu_count()} 个进程，加速比: {single_time / multi_time:.2f}x")
    print()


# ==================== 示例3：实际应用 - 批量图像处理 ====================
def example3_image_processing():
    """
    实际应用：批量图像处理
    模拟对多张图片进行CPU密集型处理
    """
    print("=" * 50)
    print("示例3：批量图像处理（模拟）")
    print("=" * 50)
    
    image_ids = list(range(1, 9))  # 8张图片
    
    # 单进程处理
    start = time.time()
    results_single = []
    for img_id in image_ids:
        result = process_image_task(img_id, size=800)
        results_single.append(result)
    single_time = time.time() - start
    print(f"单进程处理 {len(image_ids)} 张图片: {single_time:.3f}秒")
    
    # 多进程处理
    start = time.time()
    with Pool(processes=cpu_count()) as pool:
        # 使用starmap传递多个参数
        args = [(img_id, 800) for img_id in image_ids]
        results_multi = pool.starmap(process_image_task, args)
    multi_time = time.time() - start
    print(f"多进程处理 {len(image_ids)} 张图片: {multi_time:.3f}秒")
    print(f"加速比: {single_time / multi_time:.2f}x")
    
    # 显示部分结果
    print("\n处理结果示例：")
    for result in results_multi[:3]:
        print(f"  {result}")
    print()


# ==================== 示例4：进程间通信 ====================
def worker_with_return(num, return_dict, process_id):
    """
    带返回值的worker函数
    使用字典在进程间传递数据
    """
    result = is_prime(num)
    return_dict[process_id] = (num, result)


def example4_process_communication():
    """
    进程间通信示例
    使用Manager来共享数据
    """
    print("=" * 50)
    print("示例4：进程间通信")
    print("=" * 50)
    
    from multiprocessing import Manager
    
    numbers = [17, 19, 21, 23, 25, 27, 29, 31]
    
    manager = Manager()
    return_dict = manager.dict()
    
    processes = []
    for i, num in enumerate(numbers):
        p = Process(target=worker_with_return, args=(num, return_dict, i))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print("素数判断结果：")
    for i in range(len(numbers)):
        num, is_prime_result = return_dict[i]
        print(f"  {num} 是素数: {is_prime_result}")
    print()


# ==================== 最佳实践建议 ====================
def show_best_practices():
    """
    显示多进程使用的最佳实践
    """
    print("=" * 50)
    print("多进程最佳实践")
    print("=" * 50)
    print("""
1. 何时使用多进程：
   - CPU密集型任务（计算、加密、图像处理）
   - 需要真正的并行计算
   - 任务之间相对独立

2. 推荐使用进程池（Pool）：
   - 自动管理进程数量
   - 避免创建过多进程
   - 进程数通常设置为 CPU 核心数

3. 注意事项：
   - 进程间通信有开销，避免频繁通信
   - 数据序列化有成本，避免传递大对象
   - Windows 下需要使用 if __name__ == '__main__'
   - 进程启动有开销，适合长时间运行的任务

4. 当前系统信息：
   - CPU 核心数: {}
   - 推荐进程池大小: {}
""".format(cpu_count(), cpu_count()))


def main():
    """
    主函数：运行所有示例
    """
    print("\n" + "=" * 50)
    print("Python 多进程编程示例")
    print("适用于 CPU 密集型任务")
    print("=" * 50 + "\n")
    
    # 运行各个示例
    example1_basic_multiprocessing()
    example2_process_pool()
    example3_image_processing()
    example4_process_communication()
    show_best_practices()
    
    print("=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)


if __name__ == '__main__':
    # Windows 下必须使用这个保护
    main()
