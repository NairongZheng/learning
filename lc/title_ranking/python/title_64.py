# https://leetcode.cn/problems/minimum-path-sum/description

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)] # dp[i][j]: 从[0][0]到[i][j]的最小路径和
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j] # min(左边, 右边) + grid[i][j]
        return dp[-1][-1]


def main():
    test_list = [
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]],  # 7
        [[1, 2, 3], [4, 5, 6]],  # 12
    ]
    for grid in test_list:
        res = Solution().minPathSum(grid)
        print(f"res: {res}")


if __name__ == "__main__":
    main()


# 1 3 1        1 4 5
# 1 5 1        2 7 6
# 4 2 1        6 8 7
