

def isSubsequence(s, t):
    """
        判断子序列
        给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
        字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
        （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
    """

    # 动态规划(自己画个dp表看看)
    len_s = len(s) + 1
    len_t = len(t) + 1
    dp = [[0 for _ in range(len_t)] for _ in range(len_s)]  # dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]。
    for i in range(1, len_s):
        for j in range(1, len_t):
            if s[i - 1] == t[j - 1]:        # t中找到了一个字符在s中也出现了
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:                           # 相当于t要删除元素，继续匹配(就是双指针解法里，t继续移动指针)
                dp[i][j] = dp[i][j - 1]
    if dp[-1][-1] == len(s):
        return True
    return False
    # dp: [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 3]]

    # # 双指针
    # s_index = 0
    # t_index = 0
    # while s_index < len(s) and t_index < len(t):
    #     if t[t_index] == s[s_index]:
    #         t_index += 1
    #         s_index += 1
    #     else:
    #         t_index += 1
    # if s_index == len(s):
    #     return True
    # else:
    #     return False


aaa = isSubsequence(s="abc", t="ahbgdc")
print(aaa)      # True