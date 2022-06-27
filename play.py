def quick_sort2(self, nums, head, tail):
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
    self.quick_sort2(nums, head, left - 1)
    self.quick_sort2(nums, left + 1, tail)
    return nums