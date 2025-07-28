# https://leetcode.cn/problems/search-a-2d-matrix/description


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


def main():
    test_list = [
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],  # true
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13],  # false
    ]
    for nums, target in test_list:
        res = Solution().searchMatrix(nums, target)
        print(f"{res}")


if __name__ == "__main__":
    main()
