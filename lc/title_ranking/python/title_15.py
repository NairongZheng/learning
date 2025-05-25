# https://leetcode.cn/problems/3sum/description

# 参考题解：https://juejin.cn/post/6894787422807130119

from typing import List


class Solution:
    def twoSum(self, nums, start, target):
        """返回两数之和等于target的所有list（不重复）"""
        result = []
        # nums = sorted(nums) # 不用排序了，外面排序过了
        left = start
        right = len(nums) - 1
        while left < right:
            cur_left = nums[left]
            cur_right = nums[right]
            cur_sum = cur_left + cur_right
            if cur_sum < target:
                while left < right and nums[left] == cur_left:  # 提高效率
                    left += 1
            elif cur_sum > target:
                while left < right and nums[right] == cur_right:  # 提高效率
                    right -= 1
            else:
                result.append([nums[left], nums[right]])
                # 为了去重
                while left < right and nums[left] == cur_left:
                    left += 1
                while left < right and nums[right] == cur_right:
                    right -= 1
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # 方法一：直接调用twoSum
        # nums = sorted(nums)
        # result = []
        # i = 0
        # while i < len(nums):
        #     cur_val = nums[i]
        #     two_sum_res = self.twoSum(nums, i + 1, 0 - cur_val)
        #     for res in two_sum_res:
        #         res.append(cur_val)
        #         result.append(res)
        #     # 跳过第一个数字重复的情况，否则会出现重复结果
        #     while i < len(nums) and nums[i] == cur_val:
        #         i += 1
        # return result

        # 方法二：使用通用方法，调用nSum
        nums = sorted(nums)
        return self.nSum(nums, 3, 0, 0)

    def nSum(self, nums, n, start, target):
        """
        nums: 数组
        n: n个数之和
        start: 起始idx
        target: 目标和
        """
        # nums = sorted(nums) # 也是放在一开始的时候排序即可
        res = []
        nums_size = len(nums)
        if n < 2 or nums_size < n:
            return res
        if n == 2:
            return self.twoSum(nums, start, target)
        else:  # n > 2 时，递归计算 (n-1)Sum 的结果
            i = start
            while i < nums_size:
                cur_val = nums[i]
                sub_res = self.nSum(nums, n - 1, i + 1, target - cur_val)
                for sub in sub_res:
                    sub.append(cur_val)
                    res.append(sub)
                while i < nums_size and nums[i] == cur_val:
                    i += 1
        return res


def main():
    test_list = [
        [-1, 0, 1, 2, -1, -4],  # [[-1,-1,2],[-1,0,1]]
        [0, 1, 1],  # []
        [0, 0, 0],  # [[0,0,0]]
    ]
    for nums in test_list:
        res = Solution().threeSum(nums)
        print(f"{res}")


if __name__ == "__main__":
    main()
