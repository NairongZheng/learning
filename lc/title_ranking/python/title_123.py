# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(5)] for _ in range(len(prices))] # 0没有操作，1第一次买入，2第一次卖出，3第二次买入，4第二次卖出
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1]) # max(昨天没操作今天买入, 昨天就买入了)
            dp[i][2] = max(dp[i - 1][1] + prices[i], dp[i - 1][2]) # max(昨天买入今天卖出, 昨天就卖出了)
            dp[i][3] = max(dp[i - 1][2] - prices[i], dp[i - 1][3]) # max(昨天第一次卖出今天买入, 昨天就买入了)
            dp[i][4] = max(dp[i - 1][3] + prices[i], dp[i - 1][4]) # max(昨天买入今天卖出, 昨天就卖出了)
        return max(dp[-1])


def main():
    test_list = [
        [3, 3, 5, 0, 0, 3, 1, 4],  # 6
        [1, 2, 3, 4, 5],  # 4
        [7, 6, 4, 3, 1],  # 0
        [1],  # 0
    ]
    for prices in test_list:
        res = Solution().maxProfit(prices)
        print(f"{res}")


if __name__ == "__main__":
    main()
