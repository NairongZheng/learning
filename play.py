
def main():
    s = list(input().strip())
    stack = []
    for c in s:
        if stack == []:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if len(stack) == 0:
        return 0
    return ''.join(stack)

if __name__ == '__main__':
    main()