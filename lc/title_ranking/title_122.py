# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # 动态规划解法
        # dp = [[0 for _ in range(2)] for _ in range(len(prices))]  # dp[i][0]：持有, dp[i][1]：不持有。拥有的最多现金
        # dp[0][0] = -prices[0]
        # dp[0][1] = 0
        # for i in range(1, len(prices)):
        #     # # 递推公式dp[i][0]是与上一题唯一区别的地方, 因为这题一只股票可以买卖多次,  所以买入股票的时候, 可能会有之前买卖的利润
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]) # 今天持有=max(上一天就持有, 今天新持有)
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i]) # 今天不持有=max(上一天就不持有, 上一天持有今天卖出)
        # return dp[-1][1]
        
        # 非动态规划解法（贪心）
        max_profit = 0
        for i in range(1, len(prices)):
            price_diff = prices[i] - prices[i - 1] # 今天卖能卖多少钱
            max_profit += max(0, price_diff) # 利润累加
        return max_profit


def main():
    test_list = [
        [7,1,5,3,6,4], # 7
        [1,2,3,4,5], # 4
        [7,6,4,3,1], # 0
    ]
    for prices in test_list:
        res = Solution().maxProfit(prices)
        print(f"{res}")


if __name__ == '__main__':
    main()