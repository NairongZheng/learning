
# 与518比较

def coinChange(coins, amount):
    """
        零钱兑换
        给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
        如果没有任何一种硬币组合能组成总金额，返回 -1。
        你可以认为每种硬币的数量是无限的。
    """

    # 1. 确定dp数组以及下标的含义：dp[j]：凑足总额为j所需钱币的最少个数为dp[j]
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[amount] if dp[amount] < amount + 1 else -1

aaa = coinChange([1, 2, 5], 11)
print(aaa)