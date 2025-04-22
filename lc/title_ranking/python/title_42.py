# https://leetcode.cn/problems/trapping-rain-water/description

"""
关键思想：
一个位置 i 能存的水 = min(左边最大高度, 右边最大高度) - 当前高度，前提是这个值 > 0。
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        # 计算位置i左边最大高度
        left_max_list = [0 for _ in range(n)]
        left_max_list[0] = height[0]
        for i in range(1, n):
            left_max_list[i] = max(height[i], left_max_list[i - 1])
        # 计算位置i右边最大高度
        right_max_list = [0 for _ in range(n)]
        right_max_list[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max_list[i] = max(height[i], right_max_list[i + 1])
        # 计算位置i的雨水量
        result_list = [0 for _ in range(n)]
        for i in range(n):
            res = min(left_max_list[i], right_max_list[i]) - height[i]
            result_list[i] = max(0, res)
        return sum(result_list)


def main():
    test_list = [
        [0,1,0,2,1,0,1,3,2,1,2,1], # 6
        [4,2,0,3,2,5], # 9
    ]
    for height in test_list:
        res = Solution().trap(height)
        print(f"{res}")


if __name__ == '__main__':
    main()