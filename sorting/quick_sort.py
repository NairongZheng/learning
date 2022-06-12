"""
    quthor:damonzheng
    function:快速排序
    date:2022.4.23
"""

def quick_sort(alist, head, tail):
    if head >= tail:        # 迭代退出的条件
        return alist
    
    pivot = alist[head]
    low = head
    high = tail

    while low != high:
        while low < high and alist[high] > pivot:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < pivot:
            low += 1
        alist[high] = alist[low]
    alist[low] = pivot

    quick_sort(alist, head, low - 1)
    quick_sort(alist, low + 1, tail)

    return alist

def quick_sort2(data):
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data)//2]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort2(left) + [mid] + quick_sort2(right)
    else:
        return data

sorted_list1 = quick_sort([3, 2, 1, 9, 6, 5, 4], 0, 6)
sorted_list2 = quick_sort2([3, 2, 1, 9, 6, 5, 4])
print(sorted_list1)
print(sorted_list2)