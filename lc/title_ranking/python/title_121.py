# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划解法
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]  # dp[i][0]：持有, dp[i][1]：不持有。拥有的最多现金
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i]) # 今天持有=max(上一天就持有, 今天新持有)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i]) # 今天不持有=max(上一天就不持有, 上一天持有今天卖出)
        return dp[-1][1]
        
        # # 非动态规划解法
        # min_price = float("inf")
        # max_profit = 0
        # for price in prices:
        #     price_diff = price - min_price # 今天卖能卖多少钱
        #     max_profit = max(max_profit, price_diff) # 更新最高利润
        #     min_price = min(min_price, price) # 更新最低价格
        # return max_profit


def main():
    test_list = [
        [7,1,5,3,6,4], # 5
        [7,6,4,3,1], # 0
    ]
    for prices in test_list:
        res = Solution().maxProfit(prices)
        print(f"{res}")


if __name__ == '__main__':
    main()