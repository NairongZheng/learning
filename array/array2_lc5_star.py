

def longestPalindrome(s):
    """
        最长回文子串
        给你一个字符串 s，找到 s 中最长的回文子串。

        思路：
        要是两个for循环的方法，复杂度太高
        找回文串的难点在于，回文串的的长度可能是奇数也可能是偶数，解决该问题的核心是从中心向两端扩散的双指针技巧。
        如果回文串的长度为奇数，则它有一个中心字符；如果回文串的长度为偶数，则可以认为它有两个中心字符。

        (判读回文串是从两边向中间搜索，找回文串是从中心向两边展开)
    """
    def palindrome(s, l, r):
        """
            在s中搜索以s[l]和s[r]为中心的最长回文串
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1      # 双指针，向两边展开
            r += 1
        return s[l + 1: r]
    
    result = ''
    for i in range(len(s)):
        s1 = palindrome(s, i, i)        # 找以s[i]为中心的最长回文子串(奇数)
        s2 = palindrome(s, i, i + 1)    # 以s[i]和s[i+1]为中心的最长回文子串(偶数)
        if len(result) < len(s1):
            result = s1
        if len(result) < len(s2):
            result = s2
    return result

    # # 复杂度太高
    # result = ''
    # for i in range(len(s)):
    #     for j in range(i + 1):
    #         str_ = s[j: i + 1]
    #         if str_ == str_[::-1] and len(str_) > len(result):
    #             result = str_
    # return result


aaa = longestPalindrome("babad")
print(aaa)      # bab