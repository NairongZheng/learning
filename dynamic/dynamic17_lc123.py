

def maxProfit(prices):
    """
        买卖股票的最佳时机III
        给定一个数组, 它的第 i 个元素是一支给定的股票在第 i 天的价格
        设计一个算法来计算你所能获取的最大利润. 你最多可以完成 两笔 交易
        注意: 你不能同时参与多笔交易(你必须在再次购买前出售掉之前的股票)

        思路: 关键在于至多买卖两次, 这意味着可以买卖一次, 可以买卖两次, 也可以不买卖
    """
    dp = [[0] * 5 for _ in range(len(prices))]  # dp数组每天都有5个状态: 0(没有操作); 1(第一次买入); 2(第一次卖出); 3(第二次买入); 4(第二次卖出)
    dp[0][1] = -prices[0]
    dp[0][3] = -prices[0]
    for i in range(1, len(prices)):
        dp[i][0] = dp[i-1][0]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  # (1)第i天买入股票了,那么dp[i][1] = dp[i-1][0] - prices[i]; (2)第i天没有操作, 而是沿用前一天买入的状态
        dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])  # (1)第i天卖出股票了,那么dp[i][2] = dp[i - 1][1] + prices[i]; (2)第i天没有操作, 沿用前一天卖出股票的状态
        dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])  # 同理
        dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])  # 同理

    return dp[-1][4]

aaa = maxProfit([3,3,5,0,0,3,1,4])
print(aaa)              # 6