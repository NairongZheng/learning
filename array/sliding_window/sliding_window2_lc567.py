

# 定长的滑动窗口
def checkInclusion(s1, s2):
    """
        字符串的排列: 给定两个字符串s1和s2, 写一个函数来判断s2是否包含s1的排列
    """
    from collections import Counter
    start = 0
    template = Counter(s1)
    for end in range(len(s1) - 1, len(s2)):     # 这种写法可以自动更新end, 我们只要考虑什么时候更新start就可以
        if Counter(s2[start:end+1]) == template:
            return True
        start += 1              # 不等于的话就要找下一个窗口继续判断
    return False

aaa = checkInclusion('ab', 'eidbaooo')
print(aaa)