# https://leetcode.cn/problems/coin-change/description

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        如果只有1单位的硬币，那么递推式就是：min[i]=min[i-1]+1
        又由于我们不仅有1单位硬币，因此，以5单位硬币为例，对于需要面额为5时，5个1单位硬币可以用1个5单位硬币替换，需要面额为6时，即：min[6]=min[6-5]+1
        与原来的min[6]=6相对比，此可取最小值，继续进行该过程，得：min[i]=min[i-5]+1
        由此推广，得到：min[i]=min[i-s]+1
        """
        dp = [float("inf")] * (amount + 1)  # dp[i]: amount为i时所需的最少硬币个数
        dp[0] = 0  # 为0时，不需要硬币

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


def main():
    test_list = [
        [[1, 2, 5], 11],  # 3
        [[2], 3],  # -1
        [[1], 0],  # 0
    ]
    for coins, amount in test_list:
        res = Solution().coinChange(coins, amount)
        print(f"{res}")


if __name__ == "__main__":
    main()
