

def uniquePathsWithObstacles(obstacleGrid):
    """
        不同路径II
        一个机器人位于一个 m x n 网格的左上角
        机器人每次只能向下或者向右移动一步. 机器人试图达到网格的右下角
        现在考虑网格中有障碍物. 那么从左上角到右下角将会有多少条不同的路径
        网格中的障碍物和空位置分别用 1 和 0 来表示
    """
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]  # dp[i][j]的定义: 从(0,0)出发, 到(i,j)有dp[i][j]条不同的路径

    dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0      # 第一格先初始化
    if dp[0][0] == 0:                                   # 如果第一个就是障碍物, 就直接返回0
        return 0
    
    # 对第一行初始化
    for i in range(1, col):
        if obstacleGrid[0][i] != 1:
            dp[0][i] = dp[0][i - 1]         # 这个要注意, 不是直接=1, 前面一格是障碍物, 后面都过不来了
    
    # 对第一列初始化
    for i in range(1, row):
        if obstacleGrid[i][0] != 1:         # 可以像上面那么写, 或者这么写, 一遇到障碍物, 后面都是0, 不用管直接break了
            dp[i][0] = 1
        else:
            break
    
    # 开始走
    for i in range(1, row):
        for j in range(1, col):
            if obstacleGrid[i][j] != 1:                 # 如果等于1说明是障碍物, 就是0, dp的初始化就是0, 所以就不用写else了
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[row - 1][col - 1]

aaa = uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(aaa)