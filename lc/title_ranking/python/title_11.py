# https://leetcode.cn/problems/container-with-most-water/description

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            cur_res = min(height[left], height[right]) * (right - left)
            res = max(res, cur_res)
            # 双指针技巧，移动较低的一边
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


def main():
    test_list = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],  # 49
        [1, 1],  # 1
    ]
    for height in test_list:
        res = Solution().maxArea(height)
        print(f"{res}")


if __name__ == "__main__":
    main()
