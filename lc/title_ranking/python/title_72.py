# https://leetcode.cn/problems/edit-distance/description

"""
解决两个字符串的动态规划问题，一般都是用两个指针 i, j 分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模。
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        # 自底向上求解
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1
                    )
        return dp[m][n]


def main():
    test_list = [
        ["horse", "ros"],  # 3
        ["intention", "execution"],  # 5
    ]
    for word1, word2 in test_list:
        res = Solution().minDistance(word1, word2)
        print(f"{res}")


if __name__ == "__main__":
    main()
