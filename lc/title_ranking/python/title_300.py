# https://leetcode.cn/problems/longest-increasing-subsequence/description

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_len = -float("inf")
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_len = max(max_len, dp[i])
        return max_len if max_len != -float("inf") else 1


def main():
    test_list = [
        [10, 9, 2, 5, 3, 7, 101, 18],  # 4
        [0, 1, 0, 3, 2, 3],  # 4
        [7, 7, 7, 7, 7, 7, 7],  # 1
    ]
    for nums in test_list:
        res = Solution().lengthOfLIS(nums)
        print(f"res: {res}")


if __name__ == "__main__":
    main()
