

# 定长的滑动窗口
def strStr(haystack, needle):
    """
        实现strStr()
    """
    start = 0
    for end in range(len(needle) - 1, len(haystack)):   # 这是一个定长的窗口(28和567都是定长)
        # 这种写法可以自动更新end, 我们只要考虑什么时候更新start就可以
        if haystack[start:end+1] == needle:
            return start
        start += 1              # 不相等只需要移动start, end会在循环的时候自动移动
    return -1

aaa = strStr('hello', 'll')
bbb = strStr('aaaaa', 'bba')
print(aaa)
print(bbb)