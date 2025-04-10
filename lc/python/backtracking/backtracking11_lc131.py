

# 组合问题
def partition(s):
    """
        分割回文串
        给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
    """
    path = []
    result = []
    def backtracking(s, startIndex):
        if startIndex == len(s):
            result.append(path[:])
            return
        for i in range(startIndex, len(s)):
            temp = s[startIndex:i+1]
            if temp == temp[::-1]:
                path.append(temp)
                backtracking(s, i + 1)
                path.pop()
            else:
                continue
    backtracking(s, 0)
    return result

aaa = partition('aab')
print(aaa)          # [['a', 'a', 'b'], ['aa', 'b']]