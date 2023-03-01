"""
    author:damonzheng
    function:插入排序
    date:2022.4.23
"""

def inserted_sort(alist):
    for i in range(1, len(alist)):
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break
    return alist

sorted_list = inserted_sort([1, 2, 3, 5, 4])
print(sorted_list)