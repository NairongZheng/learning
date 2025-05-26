# https://leetcode.cn/problems/unique-paths-ii/description

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)] # dp[i][j]: 从[0][0]到[i][j]的路径有多少
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0      # 第一格先初始化
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]
        for j in range(1, m):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = dp[j - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


def main():
    test_list = [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],  # 2
        [[0, 1], [0, 0]],  # 1
        [[0,0],[1,1],[0,0]], # 0
    ]
    for obstacleGrid in test_list:
        res = Solution().uniquePathsWithObstacles(obstacleGrid)
        print(f"res: {res}")


if __name__ == "__main__":
    main()


# 0 0 0     1 1 1
# 0 1 0     1 0 1
# 0 0 0     1 1 2
