
"""
    和为 K 的子数组
    给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
"""

def subarraySum(nums, k):

    # 方法四：前缀和+哈希表(看不是很懂)
    # 优化方法：边算前缀和边统计，统计每一个前缀和出现的个数，然后计算到i位置（含i）的前缀和presum减去目标k在历史上出现过几次
    # 假如出现过m次，代表第i位以前（不含i）有m个连续子数组的和为presum-k，这m个和为presum-k的连续子数组
    # 每一个都可以和presum组合成presum-(presum-k)=k
    import collections
    result = 0
    pre_sum_dict = collections.defaultdict(int)
    pre_sum_dict[0] = 1

    pre_sum = 0
    for i in range(len(nums)):
        pre_sum += nums[i]
        result += pre_sum_dict[pre_sum - k]
        pre_sum_dict[pre_sum] += 1
    return result

    ################################################################
    # # 方法三：前缀和（时间复杂度O(n**2)，会超时）
    # result = 0
    # pre_sum = [0]

    # # 求前缀和数组，当然也可以用另一种方法求，见array3
    # tmp = 0
    # for i in range(len(nums)):
    #     tmp += nums[i]
    #     pre_sum.append(tmp)

    # # 求区间[i, j]的和（包含i, j）
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         sum_ = pre_sum[j + 1] - pre_sum[i]
    #         if sum_ == k:
    #             result += 1
    # return result

    ################################################################
    # # 方法二：暴力解法优化（时间复杂度O(n**2)，会超时）
    # result = 0
    # for i in range(len(nums)):
    #     sum_ = 0
    #     for j in range(i, len(nums)):
    #         sum_ += nums[j]
    #         if sum_ == k:
    #             result += 1
    # return result

    ################################################################
    # # 方法一：暴力解法（时间复杂度O(n**3)，会超时）
    # result = 0
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         if sum(nums[i: j + 1]) == k:
    #             result += 1
    # return result

aaa = subarraySum([2, -2, 3, 0, 4, -7], 0)
print(aaa)      # 4