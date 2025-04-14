# https://leetcode.cn/problems/jump-game-ii

from typing import List


"""
思路: 维护当前能够到达的最大下标位置，记为边界。我们从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        result = 0 # 记录当前走的步数
        cur_max_dis_idx = 0 # 当前下标，其实也就是当前能到达的最远下标，一个中间变量，主要还是下面这个变量
        next_max_dis_idx = 0 # 下一步能到达的最远下标
        for i in range(len(nums)):
            next_max_dis_idx = max(next_max_dis_idx, i + nums[i])
            if i == cur_max_dis_idx: # 到达边界则更新边界且结果+1
                result += 1
                cur_max_dis_idx = next_max_dis_idx
                if next_max_dis_idx >= len(nums) - 1:
                    break
        return result


def main():
    test_list = [
        [2,3,1,1,4], # 2
        [2,3,0,1,4], # 2
    ]
    for nums in test_list:
        res = Solution().jump(nums)
        print(f"{res}")


if __name__ == '__main__':
    main()