

def deleteAndEarn(nums):
    """
        删除并获得点数
        给你一个整数数组nums,
        选择任意一个nums[i], 删除它并获得nums[i]的点数. 之后, 你必须删除所有等于nums[i] - 1和nums[i] + 1的元素
        开始你拥有0个点数. 返回你能通过这些操作获得的最大点数

        分析:
        我们在原来的nums的基础上构造一个临时的数组new_nums, 这个数组以元素的值来做下标, 下标对应的元素是原来的元素的个数
        nums[2,2,3,3,3,4]--->new_nums[0,0,2,3,1]
        这样就转换成打家劫舍了
    """
    new_nums = [0 for _ in range(max(nums) + 1)]
    for num in nums:
        new_nums[num] += 1
    dp = [0 for _ in range(len(new_nums))]
    dp[0] = new_nums[0]
    dp[1] = new_nums[1]
    for i in range(2, len(new_nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + new_nums[i] * i)
    return dp[-1]


aaa = deleteAndEarn([2,2,3,3,3,4])
print(aaa)