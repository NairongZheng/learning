# https://leetcode.cn/problems/majority-element

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 空间复杂度O(1)的解法：Boyer-Moore 投票算法
        count = 0
        candidate = None    # 1. 初始化：票数统计count=0，候选元素candidate=None
        for num in nums:    # 2. 循环：遍历数组中的每个元素num，当票数为0，则假设当前数字是众数，当遇到相同的元素，票数+1，否则-1
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate    # 3. 返回值：返回candidate即为众数


def main():
    test_list = [
        [3,2,3], # 3
        [2,2,1,1,1,2,2], # 2
    ]
    for nums in test_list:
        res = Solution().majorityElement(nums)
        print(f"{res}")


if __name__ == '__main__':
    main()