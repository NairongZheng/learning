


def removeDuplicates(nums):
    """
        删除有序数组中的重复项
        给你一个升序排列的数组nums，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。元素的相对顺序应该保持一致。
        不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

        思路：
        我们让慢指针 slow 走在后面，快指针 fast 走在前面探路，找到一个不重复的元素就赋值给 slow 并让 slow 前进一步。
    """
    slow = fast = 0
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1

aaa = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(aaa)          # 5

# 运行之后的nums[0, 1, 2, 3, 4, 2, 2, 3, 3, 4]