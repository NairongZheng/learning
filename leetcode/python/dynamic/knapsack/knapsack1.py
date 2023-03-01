

def knapsack(bag_size, weight, value):
    """
        01背包
        有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
        每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
        举例：背包的最大重量为4，物品重量weight[1,3,4]，物品价值value[15,20,30]
        问背包能背的物品最大价值是多少？
    """
    # 1. 确定dp数组以及下标的含义：dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。
    # 2. 确定递推公式：(1)不放物品dp[i][j] = dp[i - 1][j]; (2)放物品dp[i][j] = dp[i - 1][j - weight[i]] + value[i]
    #       所以状态转移方程为dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    # 3. dp数组初始化：
    #       (1)如果背包容量j为0的话，即dp[i][0]，无论是选取哪些物品，背包价值总和一定为0
    #       (2)dp[0][j]，即：i为0，存放编号0的物品的时候，各个容量的背包所能存放的最大价值。
    #               那么很明显当 j < weight[0]的时候，dp[0][j] 应该是 0，因为背包容量比编号0的物品重量还小。
    #               当j >= weight[0]时，dp[0][j] 应该是value[0]，因为背包容量放足够放编号0物品。
    #       (3)其他位置的初始化：从递推公式可以看出，反正都会被覆盖，所以随便初始化

    row = len(weight)
    col = bag_size + 1
    dp = [[0 for _ in range(col)] for _ in range(row)]

    # 初始化dp数组
    for i in range(row):
        dp[i][0] = 0
    for j in range(1, col):
        if j >= weight[0]:
            dp[0][j] = value[0]
    
    # 更新dp数组：先遍历物品，再遍历背包
    for i in range(1, row):
        cur_weight = weight[i]
        cur_value = value[i]
        for j in range(1, col):
            if cur_weight > j:              # 说明背包装不下当前物品
                dp[i][j] = dp[i - 1][j]     # 所以不装当前物品
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_value)
    print(dp)       # [[0, 15, 15, 15, 15], [0, 15, 15, 20, 35], [0, 15, 15, 20, 35]]

if __name__ == '__main__':
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    knapsack(bag_size, weight, value)