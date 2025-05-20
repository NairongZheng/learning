# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            sum_res = numbers[left] + numbers[right]
            if sum_res == target:
                return [left + 1, right + 1]
            elif sum_res < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]  # 一定有解，所以这边随便写


def main():
    test_list = [
        [[2, 7, 11, 15], 9],  # [1,2]
        [[2, 3, 4], 6],  # [1,3]
        [[-1, 0], -1],  # [1,2]
    ]
    for numbers, target in test_list:
        res = Solution().twoSum(numbers, target)
        print(f"{res}")


if __name__ == "__main__":
    main()
