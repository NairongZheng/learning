"""
    author:damonzheng
    function:选择排序
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