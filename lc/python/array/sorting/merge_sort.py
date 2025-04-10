"""
    author:damonzheng
    function:合并排序
    date:2022.4.23
"""

def merge_sort(alist):
    n = len(alist)
    if n <= 1:          # 递归终止条件
        return alist
    pivot_index = n // 2
    first_list = merge_sort(alist[:pivot_index])
    second_list = merge_sort(alist[pivot_index:])

    first_index = 0
    second_index = 0
    result = []

    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] < second_list[second_index]:
            result.append(first_list[first_index])
            first_index += 1
        else:
            result.append(second_list[second_index])
            second_index += 1
    
    result += first_list[first_index:]
    result += second_list[second_index:]
    return result


sorted_list = merge_sort([3, 7, 5, 6, 9, 1])
print(sorted_list)