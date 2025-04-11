# https://leetcode.cn/problems/merge-sorted-array/description

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 < 0:
                nums1[p] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[p] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -=1
            p -= 1
        

def main():
    test_list = [
        [[1,2,3,0,0,0], 3, [2,5,6], 3], # [1, 2, 2, 3, 5, 6]
        [[1], 1, [], 0], # [1]
        [[0], 0, [1], 1], # [1]
    ]
    for nums1, m, nums2, n in test_list:
        Solution().merge(nums1, m, nums2, n)
        print(nums1)


if __name__ == '__main__':
    main()