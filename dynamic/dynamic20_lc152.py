

def maxProduct(nums):
    """
        乘积最大子数组
        给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
        子数组 是数组的连续子序列。

        dp数组还要存最小的是因为两个负数相乘可能变成很大，所以最小的也要存下来
    """
    dp = [[0] * 2 for _ in range(len(nums))]    # dp[i][0]表示最小的，dp[i][1]表示最大的
    dp[0][0] = nums[0]
    dp[0][1] = nums[0]
    min_result = nums[0]        # 最小乘积
    max_result = nums[0]        # 最大乘积
    for i in range(1, len(nums)):
        dp[i][0] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
        dp[i][1] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
        min_result = min(dp[i][0], min_result)
        max_result = max(dp[i][1], max_result)
    return max_result

aaa = maxProduct([-3, 0, 2, 3, -2, 4])
print(aaa)          # 6