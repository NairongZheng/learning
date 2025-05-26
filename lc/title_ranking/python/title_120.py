# https://leetcode.cn/problems/triangle/description

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for _ in range(n)] for _ in range(n)] # dp[i][j]: 从三角形顶部走到位置[i,j]的最小路径和
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
        for i in range(1, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i] # 对角的部分dp[i][i]只会跟dp[i - 1][i - 1]相关
        return min(dp[-1])


def main():
    test_list = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],  # 11
        [[-10]],  # -10
    ]
    for triangle in test_list:
        res = Solution().minimumTotal(triangle)
        print(f"res: {res}")


if __name__ == "__main__":
    main()

# 2              2  0  0  0
# 3 4            5  6  0  0
# 6 5 7         11 10 13  0
# 4 1 8 3       15 11 18 16