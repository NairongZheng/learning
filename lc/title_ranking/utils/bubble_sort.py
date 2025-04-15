"""
冒泡排序：
    相邻元素两两比较，把大的“冒泡”到后面。
    每一轮都会把未排序部分中最大的数放到末尾。
    时间：最坏 O(n²)，最好 O(n)（有优化），平均O(n²)
    空间：O(1)
    稳定性：稳定
"""

def bubble_sort(nums):
    for i in range(0, len(nums) - 1):
        swapped = False  # 优化：一轮没有交换说明已经有序，用来减少时间复杂度
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j] # 逐步把最大的数放到最后
                swapped = True
        if not swapped:
            break
    return nums


def main():
    nums = [5, 7, 3, 7, 2]
    sorted_list = bubble_sort(nums)
    print(sorted_list) # [2, 3, 5, 7, 7]


if __name__ == '__main__':
    main()
