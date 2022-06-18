
# 不是很懂
def search(nums, target):
    """
        搜索旋转排序数组

        我们可以在常规二分查找的时候查看当前 mid 为分割位置分割出来的两个部分 [left, mid] 和 [mid + 1, right] 哪个部分是有序的，
        并根据有序的那个部分确定我们该如何改变二分查找的上下界，因为我们能够根据有序的那部分判断出 target 在不在这个部分!!!!!!
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

aaa = search([4,5,6,7,0,1,2], 0)
print(aaa)