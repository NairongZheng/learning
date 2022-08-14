
"""
    1. O(logn)
    heapq.heappush()是往堆中添加新值，此时自动建立了小根堆
    但heapq里面没有直接提供建立大根堆的方法，可以采取如下方法：每次push时给元素加一个负号（即取相反数），此时最小值变最大值
    那么实际上的最大值就可以处于堆顶了，返回时再取负即可。

    2. O(n)
    heapq.heapfy()是以线性时间将一个列表转化为小根堆

    3. O(logn)
    heapq.heappop()是从堆中弹出并返回最小的值
"""

import heapq


def main():
    nums = [5, 4, 2, 1, 10, 7, 7]   # 原数组
    print('原数组：', nums)

    # 把nums变成小根堆有两种方式
    small1 = small2 = []

    # 1
    for num in nums:
        heapq.heappush(small1, num)
    print('小根堆1：', small1)
    
    # 2
    small2 = nums
    nums_sort2 = []
    heapq.heapify(small2)
    print('小根堆2：', small2)

    # 排序
    nums_sort1 = nums_sort2 = []
    while small1:
        nums_sort1.append(heapq.heappop(small1))
    while small1:
        nums_sort2.append(heapq.heappop(small2))
    print('排序后：', nums_sort1)


if __name__ == '__main__':
    main()
    # 原数组： [5, 4, 2, 1, 10, 7, 7]
    # 小根堆1： [1, 2, 4, 5, 10, 7, 7]
    # 小根堆2： [1, 4, 2, 5, 10, 7, 7]
    # 排序后： [1, 2, 4, 5, 7, 7, 10]