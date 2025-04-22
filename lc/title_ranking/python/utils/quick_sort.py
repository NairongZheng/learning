"""
快速排序：
    核心思路（分治）：
        选一个基准元素（pivot）
        划分（partition）：把数组分成两部分：左边都是小于等于 pivot 的元素；右边都是大于 pivot 的元素；
        递归排序左右两边
    （快排有不同实现，具体复杂度有区别。可以查看：`lc/python/array/sorting/quick_sort.py`）
    时间：最坏 O(n²)（极端划分，比如已经有序）；最好 O(nlogn) （每次均匀划分）
    空间：O(logn)（递归栈）/O(n)（使用额外空间）
    稳定性：不稳定
"""


def quick_sort_recursion_1(nums, head, tail):
    """
    原地快排，空间复杂度O(logn)（递归栈）
    """
    if head >= tail:        # 迭代退出的条件
        return nums         # 递归终止条件：如果要排序的列表只有一个元素，或者为空，都不用操作，直接返回就可以
    
    pivot = nums[head]     # 选择第一个元素作为基准元素
    left = head
    right = tail

    while left != right:
        while left < right and nums[right] >= pivot:    # 右值大于pivot，右指针左移
            right -= 1
        nums[left] = nums[right]                      # 否则，右值比pivot小，应该放在左边，就直接拿过去填坑（pivot取出来不是有一个坑嘛）

        while left < right and nums[left] <= pivot:     # 左值小于pivot，左指针右移
            left += 1
        nums[right] = nums[left]                      # 否则，左值比pivot大，应该放在右边，拿过去填刚刚那个坑

    nums[left] = pivot     # 当left==right时，循环结束，剩下的这个坑就是pivot的位置。左边都比他小，右边都比他大

    quick_sort_recursion_1(nums, head, left - 1)
    quick_sort_recursion_1(nums, left + 1, tail)

    return nums


def quick_sort_recursion_2(nums):
    """
    原地快排，空间复杂度O(n)（使用额外空间）
    """
    if len(nums) >= 2:  # 递归入口及出口
        pivot = nums[0]  # 选取基准值
        left, right = [], []  # 定义基准值左右两侧的列表
        left = [x for x in nums[1:] if x <= pivot]
        right = [x for x in nums[1:] if x > pivot]
        return quick_sort_recursion_2(left) + [pivot] + quick_sort_recursion_2(right)
    else:
        return nums


def quick_sort(nums):
    # 方法一：原地快排
    result = quick_sort_recursion_1(nums, 0, len(nums) - 1)
    
    # # 方法二：非原地快排
    # result = quick_sort_recursion_2(nums)
    
    return result


def main():
    nums = [5, 2, 3, 1, 4]
    sorted_list = quick_sort(nums)
    print(sorted_list) # [1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()