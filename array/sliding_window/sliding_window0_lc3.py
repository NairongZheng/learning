

# 不定长的滑动窗口
def lengthOfLongestSubstring(s):
    """
        无重复字符的最长子串
    """
    start = 0
    max_len = float('-inf')
    mark = set()
    for end in range(len(s)):
        while s[end] in mark:
            mark.remove(s[start])
            start += 1
        max_len = max(max_len, end - start + 1)
        mark.add(s[end])
    if max_len == float('-inf'):
        return 0
    else:
        return max_len

aaa = lengthOfLongestSubstring("pwwkew")
print(aaa)