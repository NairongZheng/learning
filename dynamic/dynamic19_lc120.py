

def minimumTotal(triangle):
    """
        三角形最小路径和
    """
    n = len(triangle)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]

    for i in range(1, n):
        for j in range(1, i):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
    return min(dp[-1])

aaa = minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(aaa)          # 11

# dp: [[[2, 0, 0, 0], [5, 6, 0, 0], [11, 10, 13, 0], [15, 11, 18, 16]]]