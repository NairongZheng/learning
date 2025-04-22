# https://leetcode.cn/problems/rotate-array/description

from typing import List
from utils.reverse_nums import reverse


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法一：三次翻转
        k = k % len(nums)
        reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])
        
        
        # # 方法二：环状替换（比较难理解）
        # n = len(nums)
        # k = k % n
        # if k == 0 or n <= 1:
        #     return
        
        # count = 0 # 记录一共移动了多少个元素
        # start = 0 # 每一个cycle的起点
        # while count < n: # 总共移动n个就结束了
        #     current = start
        #     prev_v = nums[start] # 记录中间保存下来的那个值，也就是下一个要移动的值
        #     while True:
        #         next_idx = (current + k) % n
        #         nums[next_idx], prev_v = prev_v, nums[next_idx] # 一次移动
        #         current = next_idx
        #         count += 1
                
        #         if current == start:
        #             break
        #     start += 1
        


def main():
    test_list = [
        [[1,2,3,4,5,6,7], 5], # [3,4,5,6,7,1,2]
        [[1,2,3,4,5,6], 2], # [5,6,1,2,3,4]
    ]
    for nums, k in test_list:
        Solution().rotate(nums, k)
        print(f"{nums}")


if __name__ == '__main__':
    main()