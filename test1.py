#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return string字符串
#
class Solution:
    def decodeString(self , s: str) -> str:
        # write code here
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                str_ = ''
                while stack and stack[-1] != '[':
                    str_ += stack.pop()
                stack.pop()
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                a = int(''.join(num[::-1]))
                stack.append(a * str_)
        return ''.join(stack)[::-1]

aaa = Solution()
bbb = aaa.decodeString("3[3[ac]]")
pass