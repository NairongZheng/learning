# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description


from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 法一：直接用一个dp数组，比较不好理解
        # dp[i][k][0]: k次交易后 持有 法二的buy
        # dp[i][k][1]: k次交易后 不持有 法二的sell
        dp = [[[float("-inf"), 0] for _ in range(k + 1)] for _ in range(len(prices))]
        
        dp[0][0][0] = -prices[0]

        for i in range(1, len(prices)):
            # 处理 j = 0 的情况
            dp[i][0][0] = max(dp[i - 1][0][1] - prices[i], dp[i - 1][0][0]) # 未交易，持有
            dp[i][0][1] = dp[i - 1][0][1] # 未交易，不持有
            
            for j in range(1, k + 1):
                # 状态转移方程
                dp[i][j][0] = max(dp[i - 1][j][1] - prices[i], dp[i - 1][j][0]) # 持有 = max(上一天卖今天买, 上一天买)
                dp[i][j][1] = max(dp[i - 1][j - 1][0] + prices[i], dp[i - 1][j][1]) # 不持有 = max(上一天买今天卖, 上一天卖)
        return max(dp[-1][j][1] for j in range(k + 1))

        # # 法二：用两个数组比较清晰
        # n = len(prices)
        # k = min(k, n // 2)  # 因为n天最多只能进行 n // 2 笔交易
        # buy = [[float("-inf")] * (k + 1) for _ in range(n)] # 进行恰好 k 笔交易，并且当前手上持有一支股票
        # sell = [[0] * (k + 1) for _ in range(n)] # 恰好进行 k 笔交易，并且当前手上不持有股票
        # buy[0][0] = -prices[0]
        
        # # 转移方程
        # for i in range(1, n):
        #     buy[i][0] = max(sell[i - 1][0] - prices[i], buy[i - 1][0])
        #     for j in range(1, k + 1):
        #         buy[i][j] = max(sell[i - 1][j] - prices[i], buy[i - 1][j]) # 持有 = max(上一天卖今天买, 上一天买)
        #         sell[i][j] = max(buy[i - 1][j - 1] + prices[i], sell[i - 1][j]) # 不持有 = max(上一天买今天卖, 上一天卖)
        # return max(sell[-1])


def main():
    test_list = [
        [[2, 4, 1], 2],  # 2
        [[3, 2, 6, 5, 0, 3], 2],  # 7
    ]
    for prices, k in test_list:
        res = Solution().maxProfit(k, prices)
        print(f"{res}")


if __name__ == "__main__":
    main()
