

# 组合问题
def combine(n, k):
    """
        组合
        给定两个整数n和k, 返回范围[1, n]中所有可能的k个数的组合
    """
    result = []
    path = []

    def backtracking(n, k, startIndex):

        # 结束条件
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(startIndex, n + 1):
            path.append(i)
            backtracking(n, k, i + 1)
            path.pop()                  # 回溯
    
    backtracking(n, k, 1)
    return result

aaa = combine(4, 2)
print(aaa)