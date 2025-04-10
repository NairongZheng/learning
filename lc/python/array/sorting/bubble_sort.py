"""
    author:damonzheng
    function:冒泡排序
    date:2022.4.23
"""

def bubble_sort(alist):
    for i in range(0, len(alist) - 1):
        flag = 0        # flag是用来减少时间复杂度的
        for j in range(0, len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                flag = 1
        if flag == 0:
            return alist
    return alist

sorted_list = bubble_sort([1, 2, 5, 4, 3])
print(sorted_list)