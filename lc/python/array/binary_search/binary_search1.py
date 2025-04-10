
"""
    Author:damonzheng
    Date:2022.5.29
    参考自bilibili@哈哈哈123yl(https://www.bilibili.com/video/BV1254y1B7xK?spm_id_from=333.999.0.0)
"""

# 1.时间复杂度logn
# 2.已经排序好的list里才能应用二分法
# 3.边界条件是难点也很关键

def binary_search_1(alist, target):
    """
        二分法(迭代), 写法1
    """
    left = 0
    right = len(alist) - 1
    while left < right:             # 只要是二分法, 一定写成<,不用<=. 退出的时候一定left==right
        mid = (left + right) // 2   # 永远不在循环里面判断alist[mid] == target
        if alist[mid] < target:     # left取到的区间跟right取到的区间合起来应该是整个list!!!很重要
            left = mid + 1
        else:
            right = mid
    if alist[left] == target:       # 这个就是弥补不在循环里判断alist[mid] == target
        print('found number in index of {}'.format(left))
    else:
        print('do not have this number in the list')

def binary_search_2(alist, target):
    """
        二分法(迭代), 写法2
    """
    left = 0
    right = len(alist) - 1
    while left < right:             # 只要是二分法, 一定写成<,不用<=. 退出的时候一定left==right
        mid = (left + right + 1) // 2   # 永远不在循环里面判断alist[mid] == target
        if alist[mid] > target:     # left取到的区间跟right取到的区间合起来应该是整个list!!!很重要
            right = mid - 1
        else:
            left = mid              # 当出现left==mid的时候, 一定要取右中位数避免死循环, 就是mid = (left + right + 1) // 2
    if alist[left] == target:       # 这个就是弥补不在循环里判断alist[mid] == target
        print('found number in index of {}'.format(left))
    else:
        print('do not have this number in the list')

binary_search_1([0, 1, 2, 3], 1)
binary_search_2([0, 1, 2, 3], 1)