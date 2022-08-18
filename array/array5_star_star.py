


class Difference:
    """
        差分数组工具类
    """
    def __init__(self, nums):
        """
            构造差分数组
        """
        self.nums = nums
        self.diff = [0 for _ in range(len(self.nums))]      # 差分数组
        self.diff[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.diff[i] = self.nums[i] - self.nums[i - 1]
    
    def increment(self, i, j, val):
        """
            给闭区间[i, j]，对这个区间内的所有数增加val
        """
        self.diff[i] += val
        if j + 1 < len(self.diff):  # 注意：当 j+1 >= diff.length 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 val 了。
            self.diff[j + 1] -= val
    
    def return_result(self):
        """
            一顿操作之后从diff逆推回nums变成啥样了
            也就是根据差分数组构造结果数组
        """
        result = [0 for _ in range(len(self.diff))]    # 一通乱造之后的新数组
        result[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            result[i] = result[i - 1] + self.diff[i]
        return result

aaa = Difference([0, 1, 2, 3, 4, 5, 6, 7])  # diff: [0, 1, 1, 1, 1, 1, 1, 1]
aaa.increment(0, 4, 2)                      # diff: [2, 1, 1, 1, 1, -1, 1, 1]
aaa.increment(3, 6, -1)                     # diff: [2, 1, 1, 0, 1, -1, 1, 2]
print(aaa.return_result())                  # [2, 3, 4, 4, 5, 4, 5, 7]