"""
选择排序：
    每次选择最小（或最大）的元素放到已排序部分的末尾。
    时间：始终 O(n²)
    空间：O(1)
    稳定性：不稳定（交换可能打乱顺序）如果未排序部分中有两个相同的值，这种交换操作可能会导致它们的相对顺序发生改变。
"""

def selected_sort(nums):
    for i in range(0, len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i] # 每次选择最小的元素放到已排序部分的末尾
    return nums


def main():
    nums = [5, 7, 3, 7, 2]
    sorted_list = selected_sort(nums)
    print(sorted_list) # [2, 3, 5, 7, 7]


if __name__ == '__main__':
    main()