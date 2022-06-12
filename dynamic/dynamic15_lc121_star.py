

def maxProfit(prices):
    """
        买卖股票的最佳时机
        给定一个数组prices, 它的第i个元素prices[i]表示一支给定股票第i天的价格
        你只能选择某一天买入这只股票, 并选择在未来的某一个不同的日子卖出该股票. 设计一个算法来计算你所能获取的最大利润
        返回你可以从这笔交易中获取的最大利润. 如果你不能获取任何利润, 返回0
    """
    # 动态规划
    dp = [[0] * 2 for _ in range(len(prices))]  # dp[i][0]表示第i天持有股票所得最多现金, dp[i][1]表示第i天不持有股票所得最多现金
    dp[0][0] = -prices[0]       # dp[0][0]表示第0天持有股票, 此时的持有股票就是买入股票, 所以dp[0][0] = -prices[0]
    dp[0][1] = 0                # dp[0][1]表示第0天不持有股票, 不持有股票那么现金就是0, 所以dp[0][1] = 0
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], -prices[i])    # 第i天持有股票可以由两个状态推导出来: (1)第i-1天就持有, 那么就保持现状; (2)第i天买入股票, 那么现金就是买入今天的股票后所得现金, 即-prices[i]
        dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])  # 第i天不持有股票可以由两个状态推导出来: (1)第i-1天就不持有, 那么就保持现状; (2)第i天卖出股票, 那么现金就是按照今天股票佳价格卖出后所得现金
    return dp[-1][1]

    # # 贪心算法
    # low = float('inf')
    # result = 0
    # for i in range(len(prices)):
    #     low = min(low, prices[i])
    #     result = max(result, prices[i] - low)
    # return result

aaa = maxProfit([7,1,5,3,6,4])
print(aaa)