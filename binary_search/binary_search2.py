
"""
    Author:damonzheng
    Date:2022.5.29
    参考自bilibili@哈哈哈123yl(https://www.bilibili.com/video/BV1254y1B7xK?spm_id_from=333.999.0.0)
"""

# 1.时间复杂度logn
# 2.已经排序好的list里才能应用二分法
# 3.边界条件是难点也很关键

def binary_search(alist, left, right, target):
    """
        二分法(递归)(基本不用这个)
    """

    # 结束条件
    if left == right:
        if alist[left] == target:
            print('found in index of {}'.format(left))
        else:
            print('not found')
        return

    mid = (left + right) // 2
    if alist[mid] < target:
        binary_search(alist, mid + 1, right, target)
    else:
        binary_search(alist, left, mid, target)

binary_search([0, 1, 2, 3], 0, 3, 4)