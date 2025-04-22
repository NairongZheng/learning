# https://leetcode.cn/problems/h-index/description

from typing import List


class Solution:
    def func1(self, citations: List[int]) -> int:
        # 普通：排序法：时间O(nlogn)，空间O(1)
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h
    
    def func2(self, citations: List[int]) -> int:
        # 普通：二分查找：时间O(nlogn)，空间O(1)
        left = 0
        right = len(citations)
        while left < right:
            mid = (left + right + 1) // 2 # +1 防止死循环
            count = 0
            # 每次在查找范围内取中点 mid，同时扫描整个数组，判断是否至少有 mid 个数大于 mid
            for v in citations:
                if v >= mid:
                    count += 1
            if count >= mid:
                # 如果有，说明要寻找的 h 在搜索区间的右边，即要找的答案在 [mid, right] 区间内
                left = mid
            else:
                # 反之则在左边。即要找的答案在 [0, mid) 区间内
                right = mid - 1
        return left
    
    def func3(self, citations: List[int]) -> int:
        # 进阶：桶计数法：时间O(n)，空间O(n)
        n = len(citations)
        bucket = [0] * (n + 1) # 创建一个桶数组 bucket，下标表示引用次数。
        for c in citations:
            if c >= n:
                bucket[n] += 1 # 超过总论文数的引用可以统统算作最后一个桶（因为 h 最大也不会超过 n）。
            else:
                bucket[c] += 1
        count = 0
        # 从后往前累加引用次数 ≥ i 的论文总数，看是否 ≥ i。
        for i in range(n, -1, -1):
            count += bucket[i]
            if count >= i: # 关键理解：“至少 h 篇引用 ≥ h”
                return i
        return 0
    
    def hIndex(self, citations: List[int]) -> int:
        # # 普通：排序法：时间O(nlogn)，空间O(1)
        # res = self.func1(citations)
        
        # 普通：二分查找：时间O(nlogn)，空间O(1)
        res = self.func2(citations)
        
        # # 进阶：桶计数法：时间O(n)，空间O(n)（很好理解！）
        # res = self.func3(citations)
        
        return res


def main():
    test_list = [
        [3,0,6,1,5], # 3
        [1,3,1], # 1
    ]
    for nums in test_list:
        res = Solution().hIndex(nums)
        print(f"{res}")


if __name__ == '__main__':
    main()