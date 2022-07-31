def combinationSum2(candidates, target):
    candidates.sort()
    path = []
    result = []
    sum_ = 0
    usage_list = [False for _ in range(len(candidates))]
    def backtracking(candidates, target, sum_, startIndex):
        if sum_ > target:
            return
        if sum_ == target:
            result.append(path[:])
            return
        for i in range(startIndex, len(candidates)):
            if i > 0 and usage_list[i] == usage_list[i - 1] and usage_list[i - 1] == False:
                continue
            usage_list[i] = True
            path.append(candidates[i])
            sum_ += candidates[i]
            backtracking(candidates, target, sum_, i + 1)
            sum_ -= candidates[i]
            path.pop()
            usage_list[i] = False
    backtracking(candidates, target, sum_, 0)
    return result

aaa = combinationSum2([10,1,2,7,6,1,5],8)
print(aaa)