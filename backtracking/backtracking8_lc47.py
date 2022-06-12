

# 排列
def permuteUnique(nums):
    """
        全排列II
        给定一个可包含重复数字的序列nums, 按任意顺序返回所有不重复的全排列

        关键: 可包含重复数字
    """
    path = []
    result = []
    usage_list = [False for _ in range(len(nums))]
    nums.sort()

    def backtracking(nums):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(0, len(nums)):
            if usage_list[i] == False:
                if i > 0 and nums[i] == nums[i - 1] and usage_list[i - 1] == False:
                    continue
                usage_list[i] = True
                path.append(nums[i])
                backtracking(nums)
                path.pop()
                usage_list[i] = False
    
    backtracking(nums)
    return result

aaa = permuteUnique([1,1,2])
print(aaa)