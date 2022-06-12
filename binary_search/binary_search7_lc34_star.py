
def searchRange(nums, target):
    """
        在排序数组中查找元素的第一个和最后一个位置
    """

    result = [-1, -1]
    if not nums:
        return result

    # 找左边界
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] != target:
        return result
    result[0] = left

    # 找右边界
    left = 0        # 这个也可以去掉
    right = len(nums) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    result[-1] = left
    return result

aaa = searchRange([6, 7, 7, 8, 8, 8, 20], 8)
print(aaa)
