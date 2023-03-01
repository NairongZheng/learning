
def findTargetSumWays(nums, target):
    """
        目标和
        给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。
        现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
        返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

        分析：
        本题要如何使表达式结果为target，既然为target，那么就一定有 left组合 - right组合 = target。
        left + right等于sum，而sum是固定的。
        公式来了， left - (sum - left) = target -> left = (target + sum)/2 。
        target是固定的，sum是固定的，left就可以求出来。
        此时问题就是在集合nums中找出和为left的组合。

        如何转化为01背包问题呢。
        假设加法的总和为x，那么减法对应的总和就是sum - x。
        所以我们要求的是 x - (sum - x) = S --> x = (S + sum) / 2
        此时问题就转化为，装满容量为x背包，有几种方法。
        看到(S + sum) / 2 应该担心计算的过程中向下取整有没有影响。这么担心就对了
        例如sum 是5，S是2的话其实就是无解的; 同时如果 S的绝对值已经大于sum，那么也是没有方案的。
        这次和之前遇到的背包问题不一样了，之前都是求容量为j的背包，最多能装多少。
        本题则是装满有几种方法。其实这就是一个组合问题了。
    """
    # 1. 确定dp数组以及下标的含义：dp[j] 表示：填满j（包括j）这么大容积的包，有dp[j]种方法
    # 2. 确定递推公式：求组合类问题的公式，都是类似这种：dp[j] += dp[j - nums[i]]
    # 3. dp数组如何初始化
    #       从递归公式可以看出，在初始化的时候dp[0] 一定要初始化为1，因为dp[0]是在公式中一切递推结果的起源，如果dp[0]是0的话，递归结果将都是0。
    #       dp[0] = 1，理论上也很好解释，装满容量为0的背包，有1种方法，就是装0件物品。

    sumValue = sum(nums)
    # 注意边界条件为 target>sumValue or target<-sumValue or  (sumValue + target) % 2 == 1
    if abs(target) > sumValue or (sumValue + target) % 2 == 1:
        return 0
    bagSize = (sumValue + target) // 2
    dp = [0] * (bagSize + 1)
    dp[0] = 1
    for i in range(len(nums)):
        for j in range(bagSize, nums[i] - 1, -1):
            dp[j] += dp[j - nums[i]]
    return dp[bagSize]

aaa = findTargetSumWays([1,1,1,1,1], 3)
print(aaa)