

def knapscak():
    """
        01背包(滚动数组)
        对于背包问题其实状态都是可以压缩的。
        在使用二维数组的时候，递推公式：dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);
        其实可以发现如果把dp[i - 1]那一层拷贝到dp[i]上，表达式完全可以是：dp[i][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i]);
        与其把dp[i - 1]这一层拷贝到dp[i]上，不如只用一个一维数组了，只用dp[j]（一维数组，也可以理解是一个滚动数组）。
    """
    # 1. 确定dp数组的定义：dp[j]表示：容量为j的背包，所背的物品价值可以最大为dp[j]。
    # 2. 一维dp数组的递推公式：
    #       dp[j]可以通过dp[j - weight[i]]推导出来，dp[j - weight[i]]表示容量为j - weight[i]的背包所背的最大价值。
    #       此时dp[j]有两个选择，一个是取自己dp[j] 相当于 二维dp数组中的dp[i-1][j]，即不放物品i，
    #       一个是取dp[j - weight[i]] + value[i]，即放物品i，指定是取最大的，毕竟是求最大价值，
    #       所以递归公式为：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
    #       可以看出相对于二维dp数组的写法，就是把dp[i][j]中i的维度去掉了。
    # 3. 一维dp数组如何初始化：关于初始化，一定要和dp数组的定义吻合，否则到递推公式的时候就会越来越乱。这里都初始为0就可以
    # 4. 一维dp数组遍历顺序：二维dp遍历的时候，背包容量是从小到大，而一维dp遍历的时候，背包是从大到小。
    #       倒序遍历是为了保证物品i只被放入一次！。但如果一旦正序遍历了，那么物品0就会被重复加入多次！
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    # 初始化：全为0
    dp = [0] * (bag_weight + 1)

    # 先遍历物品，再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 递推公式
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp)

knapscak()