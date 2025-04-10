

# 排列
def permute(nums):
    """
        全排列
        给定一个不含重复数字的数组nums, 返回其所有可能的全排列

        关键: 不含重复数字
    """
    path = []
    result = []
    usage_list = [False for _ in range(len(nums))]
    # nums.sort()       # 因为不包含重复的, 所以不用排序

    def backtracking(nums):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(0, len(nums)):       # 排列就要从第一个数开始遍历
            if usage_list[i]:               # 用过的数就跳过
                continue
            usage_list[i] = True
            path.append(nums[i])
            backtracking(nums)
            path.pop()
            usage_list[i] = False
    
    backtracking(nums)
    return result

aaa = permute([1,2,3])
print(aaa)