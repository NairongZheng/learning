def longestPalindrome(s):
    result = ''
    for i in range(len(s)):
        for j in range(i + 1):
            str_ = s[j:i + 1]
            if str_ == str_[::-1] and len(str_) > len(result):
                result = str_
    return result


aaa = longestPalindrome('babad')
print(aaa)