

# 组合问题
def combinationSum3(k, n):
    """
        组合总和III
        找出所有相加之和为n的k个数的组合, 且满足下列条件: 
        只使用数字1到9
        每个数字最多使用一次 
        返回所有可能的有效组合的列表. 该列表不能包含相同的组合两次, 组合可以以任何顺序返回
    """
    path = []
    result = []
    
    def backtracking(k, n, startIndex, sum_):

        # 结束条件
        if len(path) == k:
            if sum_ == n:
                result.append(path[:])
            return

        for i in range(startIndex, 10):
            path.append(i)
            sum_ += i
            backtracking(k, n, i + 1, sum_)
            sum_ -= i
            path.pop()
    
    backtracking(k, n, 1, 0)
    return result

aaa = combinationSum3(3, 9)
print(aaa)