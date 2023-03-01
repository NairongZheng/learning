

def lengthOfLIS(nums):
    """
        最长递增子序列
        给你一个整数数组 nums, 找到其中最长严格递增子序列的长度
    """
    
    if len(nums) <= 1:
        return len(nums)
    dp = [1 for _ in range(len(nums))]  # dp[i]的定义: 表示i之前包括i的以nums[i]结尾最长上升子序列的长度
    result = 0
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)   # 注意这里不是要dp[i] 与 dp[j] + 1进行比较, 而是我们要取dp[j] + 1的最大值
        result = max(result, dp[i])
    return result

aaa = lengthOfLIS([10,9,2,5,3,7,101,18])
print(aaa)      # 4