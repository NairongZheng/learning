
# 组合
def combinationSum(candidates, target):
    """
        组合总和
        给你一个无重复元素的整数数组candidates和一个目标整数target, 
        找出candidates中可以使数字和为目标数target的所有不同组合, 并以列表形式返回
        candidates中的同一个数字可以无限制重复被选取. 如果至少一个数字的被选数量不同, 则两种组合是不同的

        关键: 无重复元素, 同一个数字可以无限制重复被选取
    """
    path = []
    result = []

    def backtracking(candidates, target, sum_, startIndex):
        if sum_ > target:
            return
        if sum_ == target:
            result.append(path[:])
            return
        for i in range(startIndex, len(candidates)):
            sum_ += candidates[i]
            path.append(candidates[i])
            backtracking(candidates, target, sum_, i)       # 因为数字是可以重复的, 所以startIndex就可以从这一个开始, 不用从下一个
            path.pop()
            sum_ -= candidates[i]
    
    backtracking(candidates, target, 0, 0)
    return result

aaa = combinationSum([2,3,5], 8)
print(aaa)