

def characterReplacement(s, k):
    """
        替换后的最长重复字符
        给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
        在执行上述操作后，返回包含相同字母的最长子字符串的长度。

        参考sliding_sindow8
    """

    # # 用字典
    # adict = {}
    # max_len = float('-inf')
    # start = 0
    # for end in range(len(s)):
    #     adict[s[end]] = adict[s[end]] + 1 if s[end] in adict else 1
    #     while max(adict.values()) + k < end - start + 1:
    #         adict[s[start]] -= 1
    #         start += 1
    #     max_len = max(max_len, end - start + 1)
    # return max_len
    
    # 创个字母表
    count = [0 for _ in range(26)]
    max_len = float('-inf')
    start = 0
    for end in range(len(s)):
        count[ord(s[end]) - ord('A')] += 1
        while max(count) + k < end - start + 1:
            count[ord(s[start]) - ord('A')] -= 1
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

aaa = characterReplacement("AABABBA", 1)
print(aaa)          # 4