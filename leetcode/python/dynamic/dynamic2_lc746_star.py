

def minCostClimbingStairs(cost):
    """
        使用最小花费爬楼梯
        数组的每个下标作为一个阶梯, 第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）
        每当你爬上一个阶梯你都要花费对应的体力值, 一旦支付了相应的体力值, 你就可以选择向上爬一个阶梯或者爬两个阶梯
        请你找出达到楼层顶部的最低花费. 在开始时, 你可以选择从下标为 0 或 1 的元素作为初始阶梯
    """
    dp = [0 for _ in range(len(cost))]          # dp[i]的定义: 到达第i个台阶所花费的最小体力（注意这里认为是第一步一定是要花费）
    if len(cost) == 2:
        return min(cost[0], cost[1])
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    return min(dp[len(cost) - 1], dp[len(cost) - 2])    # 这个要注意, 不是返回dp[-1]

aaa = minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
print(aaa)      # 6

# dp: [1, 100, 2, 3, 3, 103, 4, 5, 104, 6]
