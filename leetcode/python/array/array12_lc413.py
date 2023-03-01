
"""
    如果一个数列至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
    例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
    给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
    子数组 是数组中的一个连续序列。
"""

def numberOfArithmeticSlices(nums):
    
    def cal_n(n):
        """
            如果有n个连续的等差，那么会有几个子数组
            cons中，对于长度为 n 的等差数列，其所有的长度大于等于3的子数列都是等差数列，则一共有 (n-2)(n-1)/2 个等差数列。
        """
        if n == 1:
            return 0
        n += 1
        return int((n - 2) * (n - 1) / 2)

    # 构建差分数组(跟array5略微有点不同，数组怎么构建根据需求)
    diff = []
    for i in range(len(nums) - 1):
        diff.append(nums[i + 1] - nums[i])
    
    # 计算有几个是连续的
    cons = []
    a = 1
    for i in range(1, len(diff)):
        if diff[i] == diff[i - 1]:
            a += 1
        else:
            cons.append(a)
            a = 1
    cons.append(a)

    # 给出结果
    result = 0
    for num in cons:
        result += cal_n(num)
    return result

aaa = numberOfArithmeticSlices([1, 2, 3, 4, 5, 6, 12, 14, 16])
print(aaa)      # 11

# nums: [1, 2, 3, 4, 5, 6, 12, 14, 16]
# diff: [1, 1, 1, 1, 1, 6, 2, 2]
# cons: [5, 1, 2]