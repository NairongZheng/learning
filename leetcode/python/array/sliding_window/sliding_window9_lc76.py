

def minWindow(s, t):
    """
        最小覆盖子串:
        给你一个字符串s, 一个字符串t
        返回s中涵盖t所有字符的最小子串. 如果s中不存在涵盖t所有字符的子串, 则返回空字符串""
    """
    from collections import Counter
    template_dict = Counter(t)
    window_dict = {}
    # 初始化window_key
    for each_key in template_dict:
        if each_key not in window_dict:
            window_dict[each_key] = 0
    
    def isContains(window_dict, template_dict):
        for each_key in template_dict:
            if window_dict[each_key] < template_dict[each_key]:
                return False
        return True

    start = 0
    min_len = float('inf')
    result = ""
    for end in range(len(s)):
        if s[end] in template_dict:
            window_dict[s[end]] += 1
        while isContains(window_dict, template_dict):
            if min_len > (end - start + 1):
                min_len = end - start + 1
                result = s[start:end+1]
            if s[start] in window_dict:
                window_dict[s[start]] -= 1
            start += 1
    return result

aaa = minWindow("ADOBECODEBANC", "ABC")
print(aaa)