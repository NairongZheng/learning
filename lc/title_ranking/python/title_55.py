# https://leetcode.cn/problems/jump-game/description

from typing import List


"""
思路: 贪心算法局部最优解: 每次取最大跳跃步数(取最大覆盖范围) 整体最优解: 最后得到整体最大覆盖范围, 看是否能到终点
这道题目关键点在于: 不用拘泥于每次究竟跳跳几步, 而是看覆盖范围, 覆盖范围内一定是可以跳过来的, 不用管是怎么跳的
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        i = 0
        while i <= cover:
            cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False


def main():
    test_list = [
        [2,3,1,1,4], # true
        [3,2,1,0,4], # false
    ]
    for nums in test_list:
        res = Solution().canJump(nums)
        print(f"{res}")


if __name__ == '__main__':
    main()