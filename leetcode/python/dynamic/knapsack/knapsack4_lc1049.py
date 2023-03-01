

def lastStoneWeightII(stones):
    """
        最后一块石头的重量II
        有一堆石头，每块石头的重量都是正整数。每一回合，从中选出"任意"两块石头，然后将它们一起粉碎。
        假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
        如果 x == y，那么两块石头都会被完全粉碎；
        如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
        最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

        最后dp[target]里是容量为target的背包所能背的最大重量。
        那么分成两堆石头，一堆石头的总重量是dp[target]，另一堆就是sum - dp[target]。
        相撞之后剩下的最小石头重量是 (sum - dp[target]) - dp[target]
    """
    sumweight = sum(stones)
    target = sumweight // 2
    dp = [0] * (target + 1)
    for i in range(len(stones)):
        for j in range(target, stones[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
    return sumweight - 2 * dp[target]


aaa = lastStoneWeightII([2,7,4,1,8,1])
print(aaa)