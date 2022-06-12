

# 子集
def subsetsWithDup(nums):
    """
        子集II
        给你一个整数数组nums, 其中可能包含重复元素, 请你返回该数组所有可能的子集（幂集）
        解集不能包含重复的子集. 返回的解集中, 子集可以按任意顺序排列
    """
    path = []
    result = []
    usage_list = [False for _ in range(len(nums))]
    nums.sort()

    def backtracking(nums, startIndex):
        result.append(path[:])
        if startIndex == len(nums):
            return
        
        for i in range(startIndex, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and usage_list[i - 1] == False:
                continue
            usage_list[i] = True
            path.append(nums[i])
            backtracking(nums, i + 1)
            path.pop()
            usage_list[i] = False
    
    backtracking(nums, 0)
    return result

aaa = subsetsWithDup([1,2,2])
print(aaa)