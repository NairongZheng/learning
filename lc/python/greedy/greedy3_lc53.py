
def maxSubArray(nums):
    """
        最大子数组和
        给定一个整数数组nums, 找到一个具有最大和的连续子数组(子数组最少包含一个元素), 返回其最大和
    """
    # # 贪心算法
    # result = float('-inf')
    # count = 0
    # for i in range(len(nums)):
    #     count += nums[i]
    #     if count > result:
    #         result = count
    #     if count <= 0:
    #         count = 0
    # return result

    # 动态规划
    if len(nums) == 0:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    result = dp[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        result = max(dp[i], result)
    return result

aaa = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(aaa)      # 6