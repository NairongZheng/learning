class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            nums1[m + i] = nums2[i]
        # nums1.sort()
        nums1 = self.quick_sort(nums1, 0, len(nums1) - 1)
    
    def quick_sort(self, nums, head, tail):
        if head >= tail:
            return
        pivot = nums[head]
        left = head
        right = tail
        while left != right:
            while left < right and nums[right] > pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        self.quick_sort(nums, head, left - 1)
        self.quick_sort(nums, left + 1, tail)
        return nums


aaa = Solution()
bbb = aaa.merge([1,2,3,0,0,0],3,[2,5,6],3)

nums = [1,2,2,3,6,4,4,4,5]
bbb = aaa.quick_sort(nums)
pass