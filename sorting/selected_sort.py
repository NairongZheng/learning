"""
    author:damonzheng
    function:选择排序：第一次遍历n-1个数找到最小的与第一个替换，第二次遍历n-2个数，如此循环
    date:2022.4.23
"""

def selected_sort(alist):
    min_index = 0
    for i in range(0, len(alist) - 1):
        for j in range(i, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
        min_index = i + 1
    return alist

sorted_list = selected_sort([1, 8, 6, 3, 5])
print(sorted_list)