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
print(bbb)