
# 排列/组合，多个数组取值（跟电话号码那题一样）


def permute(some_nums):

    path = []
    result = []
    def backtracking(some_nums, index):
        # if len(path) == len(some_nums):
        if index == len(some_nums):
            result.append(path[:])
            return
        
        nums = some_nums[index]
        for i in range(len(nums)):
            path.append(nums[i])
            backtracking(some_nums, index + 1)
            path.pop()
    backtracking(some_nums, 0)
    return result


aaa = permute([[1, 3], [5, 0, 6], [4, 3]])
print(aaa)
# [[1, 5, 4], [1, 5, 3], [1, 0, 4], [1, 0, 3], [1, 6, 4], [1, 6, 3], [3, 5, 4], [3, 5, 3], [3, 0, 4], [3, 0, 3], [3, 6, 4], [3, 6, 3]]