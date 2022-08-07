

def longestCommonSubsequence(text1, text2):
    """
        最长公共子序列
        给定两个字符串 text1 和 text2, 返回这两个字符串的最长公共子序列的长度
        一个字符串的 子序列 是指这样一个新的字符串：
        它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串
    """
    
    # dp[i][j]的定义: 长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]       # dp: [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 3]]

aaa = longestCommonSubsequence('abcde', 'ace')
print(aaa)      # 3