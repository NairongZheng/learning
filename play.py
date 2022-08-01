
def knapsack(bag_size, weight, value):
    
    dp = [0 for _ in range(bag_size + 1)]
    for i in range(len(weight)):
        for j in range(bag_size, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    pass


if __name__ == '__main__':
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    knapsack(bag_size, weight, value)