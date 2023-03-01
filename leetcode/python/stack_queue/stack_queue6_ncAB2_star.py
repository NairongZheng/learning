

def IsPopOrder(pushV, popV):
    """
        栈的压入弹出
    """
    # 这个比较好理解吧
    stack = []
    index = 0
    for i in range(len(pushV)):
        if pushV[i] != popV[index]:
            stack.append(pushV[i])
        else:
            index += 1
            while stack and popV[index] == stack[-1]:
                stack.pop()
                index += 1
    while index < len(popV):
        if popV[index] == stack.pop():
            index += 1
        else:
            return False
    return True


    # n = len(pushV)
    # stack = []
    # j = 0
    # for i in range(n):
    #     while j < n and (len(stack) == 0 or stack[-1] != popV[i]):
    #         stack.append(pushV[j])
    #         j += 1
    #     if stack[-1] == popV[i]:
    #         stack.pop()
    #     else:
    #         return False
    # return True

aaa = IsPopOrder([1,2,3,4,5],[4,5,3,2,1])
bbb = IsPopOrder([1,2,3,4,5],[4,3,5,1,2])
print(aaa)      # True
print(bbb)      # False