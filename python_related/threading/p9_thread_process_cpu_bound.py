"""
    使用多进程multiprocessing模块加速程序的运行（CPU密集型计算）
"""

import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [11227253509529] * 100


def is_prime(n):
    """
        判断是不是素数
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    squrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, squrt_n + 1, 2):
        if n % i == 0:
            return False


def single_thread():
    """
        单线程计算
    """
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    """
        用线程池实现多线程计算
    """
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    """
        用进程池实现多进程计算
    """
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def main():
    # 单线程计算需要的时间
    start = time.time()
    single_thread()
    end = time.time()
    print('single_thread, cost:', end - start, 'seconds')

    # 多线程计算需要的时间
    start = time.time()
    multi_thread()
    end = time.time()
    print('multi_thread, cost:', end - start, 'seconds')

    # 多进程计算需要的时间
    start = time.time()
    multi_process()
    end = time.time()
    print('multi_process, cost:', end - start, 'seconds')

    # single_thread, cost: 16.638298749923706 seconds
    # multi_thread, cost: 16.15305757522583 seconds         # 多线程没有比单线程快，因为要一直调用CPU计算（多次调用IO用多线程就快）
    # multi_process, cost: 3.4207210540771484 seconds       # 这种情况用多进程就能快很多


if __name__ == '__main__':
    main()