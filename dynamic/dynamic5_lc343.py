

def integerBreak(n):
    """
        整数拆分
        给定一个正整数 n, 将其拆分为至少两个正整数的和, 并使这些整数的乘积最大化. 返回你可以获得的最大乘积
    """
    dp = [0 for _ in range(n + 1)]      # dp[i]的定义: 分拆数字i, 可以得到的最大乘积为dp[i]. 但是其实dp[0]跟dp[1]是没意义的
    dp[2] = 1
    for i in range(3, n + 1):
        # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
        # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
        # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]
        for j in range(1, i - 1):
            dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))     # 注意这里还要跟dp[i]比大小!!!自己看看循环就懂了
    return dp[n]

aaa = integerBreak(10)
print(aaa)