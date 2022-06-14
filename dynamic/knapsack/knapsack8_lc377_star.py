
# 不是很懂
class Solution:
    def __init__(self):
        self.count = 0
        self.path = []
        self.result = []

    def combinationSum4(self, nums, target):
        """
            组合总和IV
            给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
        """
        # 4. 确定遍历顺序
        #       如果求组合数就是外层for循环遍历物品，内层for遍历背包。
        #       如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        #       如果把遍历nums（物品）放在外循环，遍历target的作为内循环的话，举一个例子：计算dp[4]的时候，
        #       结果集只有 {1,3} 这样的集合，不会有{3,1}这样的集合，因为nums遍历放在外层，3只能出现在1后面！

        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[-1]
        

        # # 回溯会超时
        # def backtracking(nums, target, startIndex):
        #     if target < 0:
        #         return
        #     if target == 0:
        #         self.result.append(self.path[:])
        #         self.count += 1
            
        #     for i in range(startIndex, len(nums)):
        #         self.path.append(nums[i])
        #         target -= nums[i]
        #         backtracking(nums, target, 0)
        #         target += nums[i]
        #         self.path.pop()
        # backtracking(nums, target, 0)
        # return self.count

aaa = Solution()
bbb = aaa.combinationSum4([1,2,3], 4)
print(bbb)