

def findMin(nums):
    """
        寻找旋转排序数组中的最小值II(有重复值)
        这个可以看视频
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:     # 等号不可以放这里的示例可以看这个[1,3,3]
            left = mid + 1
        elif nums[mid] == nums[right]:  # 这个等号放到上面还是下面都不行, 所以单独写一个
            right = right - 1
        else:                           # 等号不可以放这里的示例可以看这个[2,2,1,2]
            right = mid
    return nums[left]

aaa = findMin([2,2,2,0,1,2])
print(aaa)