

def maximalSquare(matrix):
    """
        最大正方形
        在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
    """
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]      # dp[i][j]表示以matrix[i][j]为右下角且只包含1的正常行的边长最大值
    for i in range(m):
        if matrix[i][0] == '1':
            dp[i][0] = 1
    for i in range(1, n):
        if matrix[0][i] == '1':
            dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1    # 这个转移方程看lc1227的推导
    result = max(max(row) for row in dp)
    return result ** 2