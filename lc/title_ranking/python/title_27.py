# https://leetcode.cn/problems/remove-element/description

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k], nums[i] = nums[i], nums[k] # 可以直接赋值不用交换
                k += 1
        return k


def main():
    test_list = [
        [[3,2,2,3], 3], # 2
        [[0,1,2,2,3,0,4,2], 2], # 5
        [[3,3], 5], # 2
    ]
    for nums, val in test_list:
        res = Solution().removeElement(nums, val)
        print(f"{res}: {nums}")


if __name__ == '__main__':
    main()