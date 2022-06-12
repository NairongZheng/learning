

def uniquePaths(m, n):
    """
        不同路径
        一个机器人位于一个 m x n 网格的左上角
        机器人每次只能向下或者向右移动一步. 机器人试图达到网格的右下角
        问总共有多少条不同的路径
    """
    dp = [[1 for _ in range(n)] for _ in range(m)]  # dp[i][j]的定义: 从(0,0)出发, 到(i,j)有dp[i][j]条不同的路径
    # 这边初始化要知道, dp[i][0]一定都是1, dp[0][j]也一定都是1, 所以直接把整个dp数组初始化为1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]         # return dp[-1][-1]

aaa = uniquePaths(3, 7)
print(aaa)