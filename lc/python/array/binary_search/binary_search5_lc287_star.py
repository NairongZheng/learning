

def findDuplicate(nums):
    """
        寻找重复数字(这个数组有且只有一个数是重复的)
        (不能更改原数组, 时间复杂度小于O(n**2))
        这题可以去看一下视频

        重点！！这个问题使用「二分查找」是在数组 [1, 2,.., n] 中查找一个整数，而 并非在输入数组数组中查找一个整数。
    """
    left = 1    # left=0也可以，但是用1比较好理解
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        if count > mid:
            right = mid
        else:
            left = mid + 1
    return left


aaa = findDuplicate([1, 2, 5, 2, 3, 4, 6, 2])
print(aaa)      # 2
