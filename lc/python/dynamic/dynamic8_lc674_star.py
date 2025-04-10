

def findLengthOfLCIS(nums):
    """
        最长连续递增序列
    """
    if len(nums) == 0:
        return 0
    
    result = 0
    dp = [1 for _ in range(len(nums))]      # dp[i]的定义: 以下标i为结尾的数组的连续递增的子序列长度为dp[i]
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            dp[i + 1] = dp[i] + 1
        result = max(result, dp[i + 1])
    return result

aaa = findLengthOfLCIS([1,3,5,4,7])
print(aaa)