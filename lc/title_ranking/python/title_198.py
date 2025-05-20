# https://leetcode.cn/problems/house-robber/description

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]  # i抢劫能获得的最大金额
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) # 本次抢劫能获得的最大金额=max(上一次抢劫, 上上次抢劫+这次抢劫)
        return dp[-1]


def main():
    test_list = [
        [1, 2, 3, 1],  # 4
        [2, 7, 9, 3, 1],  # 12
    ]
    for nums in test_list:
        res = Solution().rob(nums)
        print(f"{res}")


if __name__ == "__main__":
    main()
