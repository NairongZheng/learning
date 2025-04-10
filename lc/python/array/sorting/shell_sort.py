"""
    author:damonzheng
    function:希尔排序
    date:2022.4.23
"""

def shell_sort(alist):
    gap = len(alist) // 2
    while gap >= 1:
        for i in range(gap, len(alist)):
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist
sorted_list = shell_sort([1, 3, 2, 5, 4])
print(sorted_list)