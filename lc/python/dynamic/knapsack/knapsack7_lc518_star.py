
# 与377比较, 然后看看518
class Solution:
    def __init__(self):
        self.count = 0

    def change(self, amount, coins):
        """
            零钱兑换II
            给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
        """
        # 1. 确定dp数组以及下标的含义：dp[j]：凑成总金额j的货币组合数为dp[j]

        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]

        # # 回溯，会超时
        # def backtracking(amount, coins, startIndex):
        #     if amount < 0:
        #         return
        #     if amount == 0:
        #         self.count += 1
        #         return
        #     for i in range(startIndex, len(coins)):
        #         amount -= coins[i]
        #         backtracking(amount, coins, i)
        #         amount += coins[i]
        # backtracking(amount, coins, 0)
        # return self.count

aaa = Solution()
bbb = aaa.change(5, [1, 2, 5])
print(bbb)