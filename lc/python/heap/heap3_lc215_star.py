
# 注意与5的区别

"""
    数组中的第K个最大元素
    给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
    请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

    思路：
    直接用一个大根堆，每次弹出最大的，弹k次就是第k大的
"""

class Solution:
    def findKthLargest(self, nums, k):

        # 法二：堆
        # 时间复杂度O(nlogn), 空间复杂度O(logn)
        import heapq
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k):
            result = -heapq.heappop(nums)
        return result

        # # 法一：排序
        # # 快排的时间复杂度O(nlogn), 空间(递归使用栈空间)复杂度O(logn)
        # # 本题用快排时间复杂度可以做到O(n), 详见官方解析
        # self.quick_sort(nums, 0, len(nums) - 1)
        # return nums[-k]
    
    def quick_sort(self, nums, head, tail):
        if head >= tail:
            return nums
        pivot = nums[head]
        left = head
        right = tail
        while left != right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        self.quick_sort(nums, head, left - 1)
        self.quick_sort(nums, left + 1, tail)
        return nums

aaa = Solution()
bbb = aaa.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(bbb)          # 4