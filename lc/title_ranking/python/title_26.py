# https://leetcode.cn/problems/remove-duplicates-from-sorted-array

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 写法一：直接for循环，好控制边界
        if len(nums) <= 1:
            return len(nums)
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow - 1]:
                nums[slow], nums[fast] = nums[fast], nums[slow] # 可以直接赋值不用交换
                slow += 1
        return slow

        # # 写法二：快慢指针
        # if not nums:
        #     return 0
        
        # slow = 0
        # fast = 0
        # while fast < len(nums):
        #     if nums[fast] != nums[slow]:
        #         slow += 1
        #         nums[slow], nums[fast] = nums[fast], nums[slow] # 可以直接赋值不用交换
        #     fast += 1
        # return slow + 1


def main():
    test_list = [
        [1,1,2], # 2
        [0,0,1,1,1,2,2,3,3,4], # 5
    ]
    for nums in test_list:
        res = Solution().removeDuplicates(nums)
        print(f"{res}")


if __name__ == '__main__':
    main()