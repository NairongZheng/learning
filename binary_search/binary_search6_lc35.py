
def searchInsert(nums, target):
    """
        插入搜索位置
    """
    left = 0
    right = len(nums) - 1
    if nums[-1] < target:
        return len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

aaa = searchInsert([1, 3, 5, 6], 5)
print(aaa)