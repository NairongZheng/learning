# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 写法一：直接for循环，好控制边界
        if len(nums) <= 2:
            return len(nums)

        slow = 2  # 前两个元素都可以保留
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow], nums[fast] = nums[fast], nums[slow] # 可以直接赋值不用交换
                slow += 1
        return slow

        # # 写法二：快慢指针
        # if len(nums) <= 2:
        #     return len(nums)
        
        # slow = 0
        # fast = 0
        # while fast < len(nums):
        #     current = nums[fast]
        #     count = 0
        #     while fast < len(nums) and nums[fast] == current:
        #         if count < 2:
        #             nums[slow], nums[fast] = nums[fast], nums[slow] # 可以直接赋值不用交换
        #             slow += 1
        #         count += 1
        #         fast += 1
        # return slow


def main():
    test_list = [
        [1,1,1,2,2,3], # 5
        [0,0,1,1,1,1,2,3,3], # 7
    ]
    for nums in test_list:
        res = Solution().removeDuplicates(nums)
        print(f"{res}")


if __name__ == '__main__':
    main()