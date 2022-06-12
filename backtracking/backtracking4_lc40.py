

# 组合
def combinationSum2(candidates, target):
    """
        组合总和II
        给定一个候选人编号的集合candidates和一个目标数target, 找出candidates中所有可以使数字和为target的组合
        candidates中的每个数字在每个组合中只能使用一次

        关键: 每个数字在每个组合中只能使用一次
    """
    path = []
    result = []
    # 这种只能用一次的题目, 基本都是要排序, 然后用一个usage_list标记哪些数字是用过的
    candidates.sort()
    usage_list = [False for _ in range(len(candidates))]

    def backtracking(candidates, target, sum_, startIndex):
        if sum_ > target:
            return
        if sum_ == target:
            result.append(path[:])
            return
        for i in range(startIndex, len(candidates)):
            # 如果这个数字跟上一个数字是一样的, 就要判断要不要跳过
            # used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
            # used[i - 1] == false，说明同一树层candidates[i - 1]使用过
            if i > 0 and candidates[i] == candidates[i - 1] and usage_list[i - 1] == False:
                continue
            sum_ += candidates[i]
            path.append(candidates[i])
            usage_list[i] = True
            backtracking(candidates, target, sum_, i + 1)
            usage_list[i] = False
            path.pop()
            sum_ -= candidates[i]

    backtracking(candidates, target, 0, 0)
    return result

aaa = combinationSum2([10,1,2,7,6,1,5], 8)
print(aaa)
