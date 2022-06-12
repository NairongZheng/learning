

def rob(nums):
    """
        打家劫舍
        你是一个专业的小偷, 计划偷窃沿街的房屋. 每间房内都藏有一定的现金, 影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统, 
        如果两间相邻的房屋在同一晚上被小偷闯入, 系统会自动报警
        给定一个代表每个房屋存放金额的非负整数数组, 计算你不触动警报装置的情况下, 一夜之内能够偷窃到的最高金额
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0 for _ in range(len(nums))]      # dp[i]的定义: 考虑下标i(包括i)以内的房屋, 最多可以偷窃的金额为dp[i]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        # 假设第i个不偷, 那么就是dp[i - 1]; 假设第i个偷, 那么就是dp[i - 2] + nums[i], 因为不能连着偷两个
        # 所以dp[i]就是取第i个偷与不偷的最大值
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]

aaa = rob([1,2,3,1])
print(aaa)