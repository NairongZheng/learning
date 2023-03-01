

# 子集
def subsets(nums):
    """
        子集
        给你一个整数数组nums, 数组中的元素互不相同. 返回该数组所有可能的子集（幂集）
        解集不能包含重复的子集. 你可以按任意顺序返回解集
    """

    path = []
    result = []

    def backtracking(nums, startIndex):
        result.append(path[:])
        if startIndex == len(nums):
            return
        
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            backtracking(nums, i + 1)
            path.pop()
    backtracking(nums, 0)
    return result

aaa = subsets([1,2,3])
print(aaa)