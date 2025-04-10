

def knapsack(bag_size, weight, value):
    """
        完全背包
        有N件物品和一个最多能背重量为W的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
        每件物品都有无限个（也就是可以放入背包多次），求解将哪些物品装入背包里物品价值总和最大。
        完全背包和01背包问题唯一不同的地方就是，每种物品有无限件。

        我们知道01背包内嵌的循环是从大到小遍历，为了保证每个物品仅被添加一次。
        而完全背包的物品是可以添加多次的，所以要从小到大去遍历
    """
    dp = [0] * (bag_size + 1)
    for i in range(len(weight)):
        for j in range(weight[i], bag_size + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp[bag_size])

if __name__ == '__main__':
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    knapsack(bag_size, weight, value)