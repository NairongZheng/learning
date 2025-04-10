

def findAnagrams(s, p):
    """
        找到字符串中所有字母异位词
        给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
        异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
    """

    # 滑动窗口
    from collections import Counter
    result = []
    target_dict = Counter(p)
    now_dict = Counter(s[0:len(p)])
    if target_dict == now_dict:
        result.append(0)
    start = 0
    for end in range(len(p), len(s)):
        if s[end] in now_dict:
            now_dict[s[end]] += 1
        else:
            now_dict[s[end]] = 1
        now_dict[s[start]] -= 1
        if now_dict[s[start]] == 0:     # 不要忘了这个
            del(now_dict[s[start]])
        start += 1
        if target_dict == now_dict:
            result.append(start)
    return result

    # # 暴力解法，力扣上运行时间是滑动窗口的30几倍
    # from collections import Counter
    # result = []
    # target_dict = Counter(p)
    # for i in range(len(s)):
    #     if s[i] in target_dict:
    #         now_dict = Counter(s[i:i+len(p)])
    #         if now_dict == target_dict:
    #             result.append(i)
    # return result


aaa = findAnagrams("cbaebabacd", "abc")
print(aaa)      # [0, 6]