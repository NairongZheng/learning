
def isValid(s):
    stack = []
    for item in s:
        if item == '[':
            stack.append(']')
        elif item == '(':
            stack.append(')')
        elif item == '{':
            stack.append('}')
        else:
            if len(stack) == 0 or stack.pop() != item:
                return False
    if len(stack) != 0:
        return False
    return True

if __name__ == '__main__':
    # 每个s都是一个测试案例
    # s = '[]{}()'  # 正确的用例
    s = '({[)})'    # 左右不符合的用例
    s = '['         # 缺少右边括号的用例
    s = '[])'       # 缺少左边括号的用例        这个就走到了！！！！
    result = isValid(s)
    print(result)