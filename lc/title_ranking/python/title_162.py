# https://leetcode.cn/problems/find-peak-element/description


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 判断 mid 是不是峰值：
            # 左边比它小（或者 mid 是第一个元素），且右边比它小（或者 mid 是最后一个元素）
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] < nums[mid]):
                return mid
            # 如果左边比当前大，说明峰值在左边
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            # 否则峰值在右边
            else:
                left = mid + 1


def main():
    test_list = [
        [1,2,3,1],  # 2
        [1,2,1,3,5,6,4],  # 1或5
    ]
    for nums in test_list:
        res = Solution().findPeakElement(nums)
        print(f"{res}")


if __name__ == "__main__":
    main()
