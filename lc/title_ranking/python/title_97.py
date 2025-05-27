# https://leetcode.cn/problems/interleaving-string/description


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len1 + len2 != len3:
            return False
        dp = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        dp[0][0] = True
        for i in range(1, len1 + 1):  # 初始化第一列
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
        for j in range(1, len2 + 1):  # 初始化第一行
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]


def main():
    test_list = [
        ["aabcc", "dbbca", "aadbbcbcac"],  # true
        ["aabcc", "dbbca", "aadbbbaccc"],  # false
        ["", "", ""],  # true
    ]
    for s1, s2, s3 in test_list:
        res = Solution().isInterleave(s1, s2, s3)
        print(f"{res}")


if __name__ == "__main__":
    main()


# aadbbcbcac

#   N d b b c a
# N T F F F F F
# a T F F F F F
# a T T T T T F
# b F T T F T F
# c F F T T T T
# c F F F T F T
