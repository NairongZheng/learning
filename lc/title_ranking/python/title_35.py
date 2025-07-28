# https://leetcode.cn/problems/search-insert-position/description


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


def main():
    test_list = [
        [[1, 3, 5, 6], 5],  # 2
        [[1, 3, 5, 6], 2],  # 1
        [[1, 3, 5, 6], 7],  # 4
    ]
    for nums, target in test_list:
        res = Solution().searchInsert(nums, target)
        print(f"{res}")


if __name__ == "__main__":
    main()
