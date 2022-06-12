

def partitionLabels(s):
    """
        划分字母区间
        字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
        返回一个表示每个字符串片段的长度的列表。

        思路：
        统计每一个字符最后出现的位置
        从头遍历字符，并更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等了，则找到了分割点
    """
    hash = [0] * 26             # 记录每个字母出现的最远下标
    for i in range(len(s)):
        hash[ord(s[i]) - ord('a')] = i

    left = 0
    right = 0
    result = []
    for i in range(len(s)):
        right = max(right, hash[ord(s[i]) - ord('a')])      # 找到字符出现的最远边界
        if i == right:
            result.append(right - left + 1)
            left = i + 1
    return result

aaa = partitionLabels("ababcbacadefegdehijhklij")
print(aaa)
