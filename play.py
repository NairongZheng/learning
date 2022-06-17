class Solution:
    def maxDistance(self, nums1, nums2) -> int:
        max_range = 0
        for i in range(len(nums1)):
            target = nums1[i]
            target_index = self.search(nums2, target, i)
            if target_index == i and target_index == -1:
                continue
            else:
                max_range = max(max_range, target_index - i)
        return max_range
    
    def search(self, nums, target, index):
        if index > len(nums) - 1:
            return -1
        left = index
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] < target:
                right = mid - 1
            else:
                left = mid
        if target > nums[left]:
            return - 1
        return left

aaa = Solution()
# bbb = aaa.search([100,20,20,20,15,10,10,6,6,6,5,4], 14, 0)
bbb = aaa.maxDistance([2,2,2], [10,10,1])
print(bbb)