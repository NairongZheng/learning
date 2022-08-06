"""
    字母大小写全排列
    给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
"""

class Solution:
    def letterCasePermutation(self, s):

        path = []
        result = []

        def backtracking(s, startIndex):
            if len(path) == len(s):
                result.append("".join(path[:]))
                return
            
            c = s[startIndex]
            if c.isdigit():
                path.append(c)
                backtracking(s, startIndex + 1)
                path.pop()
            else:
                path.append(c.lower())
                backtracking(s, startIndex + 1)
                path.pop()

                path.append(c.upper())
                backtracking(s, startIndex + 1)
                path.pop()
        backtracking(s, 0)
        return result

aaa = Solution()
bbb = aaa.letterCasePermutation("a1b2")
print(bbb)      # ['a1b2', 'a1B2', 'A1b2', 'A1B2']