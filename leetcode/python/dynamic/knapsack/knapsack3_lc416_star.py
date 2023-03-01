

def canPartition(nums):
    """
        分割等和子集
        给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
        示例 1: 输入: [1, 5, 11, 5] 输出: true 解释: 数组可以分割成 [1, 5, 5] 和 [11].
        示例 2: 输入: [1, 2, 3, 5] 输出: false 解释: 数组不能分割成两个元素和相等的子集.

        要明确本题中我们要使用的是01背包，因为元素我们只能用一次。
        只有确定了如下四点，才能把01背包问题套到本题上来。
            背包的体积为sum / 2
            背包要放入的商品（集合里的元素）重量为 元素的数值，价值也为元素的数值
            背包如果正好装满，说明找到了总和为 sum / 2 的子集。
            背包中每一个元素是不可重复放入。
    """
    # 1. 确定dp数组以及下标的含义：
    #       01背包中，dp[j] 表示： 容量为j的背包，所背的物品价值可以最大为dp[j]。
    #       套到本题，dp[j]表示 背包总容量是j，最大可以凑成j的子集总和为dp[j]。
    # 2. 确定递推公式：
    #       01背包的递推公式为：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
    #       本题，相当于背包里放入数值，那么物品i的重量是nums[i]，其价值也是nums[i]。
    #       所以递推公式：dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]);
    # 3. dp数组如何初始化：
    #       从dp[j]的定义来看，首先dp[0]一定是0。
    #       如果如果题目给的价值都是正整数那么非0下标都初始化为0就可以了，如果题目给的价值有负数，那么非0下标就要初始化为负无穷。
    #       这样才能让dp数组在递归公式的过程中取的最大的价值，而不是被初始值覆盖了。
    #       本题题目中 只包含正整数的非空数组，所以非0下标的元素初始化为0就可以了。
    # 5. 举例推导dp数组：
    #       dp[j]的数值一定是小于等于j的。如果dp[j] == j 说明，集合中的子集总和正好可以凑成总和j，理解这一点很重要。

    target = sum(nums)
    if target % 2 == 1:
        return False
    target //= 2

    # 题目中说：每个数组中的元素不会超过 100，数组的大小不会超过 200
    # 总和不会大于20000，背包最大只需要其中一半，所以10001大小就可以了
    dp = [0] * 10001
    for i in range(len(nums)):
        for j in range(target, nums[i] - 1, -1):            # 循环从哪里到哪里要理解
            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
    return target == dp[target]

aaa = canPartition([1,5,11,5])
print(aaa)