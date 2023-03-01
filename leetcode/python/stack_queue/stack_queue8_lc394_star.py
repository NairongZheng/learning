

def decodeString(s):
    """
        字符串解码

        输入：s = "3[a]2[bc]"
        输出："aaabcbc"

        输入：s = "3[a2[c]]"
        输出："accaccacc"
    """
    stack = []
    num = ''
    for i in range(len(s)):
        if s[i] != ']':             # 遇到 ] 之前都入栈
            stack.append(s[i])
        else:
            str_ = ''
            num = ''
            while stack and stack[-1] != '[':       # 取出本次要乘数字的字串
                str_ += stack.pop()
            stack.pop()                             # 把对应的 [ 弹掉
            while stack and stack[-1].isnumeric():  # 取出要乘的倍数
                num += stack.pop()
            num = int(num[::-1])                    # 注意，弹出是逆序的，所以要倒序一下
            stack.append(str_ * num)                # 操作完之后再入栈（可能外面还套了一层 []）
    for i in range(len(stack)):                     # 遍历结束之后，栈中就只剩下几个字符串了，但是每个字符串都是逆序的，恢复一下
        stack[i] = stack[i][::-1]
    return ''.join(stack)                           # 拼一起后返回

aaa = decodeString("2[a2[cd]]")
print(aaa)      # acdcdacdcd