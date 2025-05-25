# https://leetcode.cn/problems/minimum-size-subarray-sum/description

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        start = 0
        cur_sum = 0
        for end in range(len(nums)):
            cur_sum += nums[end]
            while cur_sum >= target:
                min_len = min(min_len, end - start + 1)
                cur_sum -= nums[start]
                start += 1
        return min_len if min_len != float("inf") else 0


def main():
    test_list = [
        [7, [2, 3, 1, 2, 4, 3]],  # 2
        [4, [1, 4, 4]],  # 1
        [11, [1, 1, 1, 1, 1, 1, 1, 1]],  # 0
    ]
    for target, nums in test_list:
        res = Solution().minSubArrayLen(target, nums)
        print(f"{res}")


if __name__ == "__main__":
    main()
