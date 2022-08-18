
"""
    区域和检索 - 数组不可变
    给定一个整数数组  nums，处理以下类型的多个查询:
    计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
"""

class NumArray:
    """
        核心思路是我们创建一个新数组pre_sum，presum[i]记录nums[0:i-1]的累加和
        这样，sumRange 函数仅仅需要做一次减法运算，避免了每次进行 for 循环调用，最坏时间复杂度为常数 O(1)。
    """
    
    def __init__(self, nums):

        self.nums = nums
        self.pre_sum = [0]
        for i in range(1, len(nums) + 1):
            self.pre_sum.append(self.pre_sum[i - 1] + self.nums[i - 1])

        # # 法一：速度慢
        # self.nums = nums

    def sumRange(self, left, right):
        # pre_sum[left]记录的是[0, left-1]的累加和
        # pre_sum[right + 1]记录的是[0, right]的累加和
        # 二者一减就是答案(建议在纸上把两个数组画出来看看)
        return self.pre_sum[right + 1] - self.pre_sum[left]

        # # 法一：速度慢
        # # 这样，可以达到效果，但是效率很差，因为 sumRange 方法会被频繁调用，而它的时间复杂度是 O(N)，其中 N 代表 nums 数组的长度。
        # # 这道题的最优解法是使用前缀和技巧，将 sumRange 函数的时间复杂度降为 O(1)，说白了就是不要在 sumRange 里面用 for 循环
        # result = 0
        # for i in range(left, right + 1):
        #     result += self.nums[i]
        # return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

obj = NumArray(nums=[-2, 0, 3, -5, 2, -1])
aaa = obj.sumRange(0, 5)
print(aaa)      # -3

# [-2, 0, 3, -5, 2, -1]         # nums
# [0, -2, -2, 1, -4, -2, -3]    # pre_sum