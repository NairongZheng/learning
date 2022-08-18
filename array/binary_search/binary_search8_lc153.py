

def findMin(nums):
    """
        寻找旋转排序数组中的最小值
        虽然这不是一个递增数组, 但是是部分递增的
        可以看看视频
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

aaa = findMin([3, 5, 4, 1, 2])
print(aaa)