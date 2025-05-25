# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = -float("inf")
        aset = set()
        start = 0
        for end in range(len(s)):
            while s[end] in aset:  # 如果当前字符已经出现过了，就要开始移动start指针了
                aset.remove(s[start])
                start += 1
            aset.add(s[end])
            max_len = max(max_len, end - start + 1)
        return max_len if max_len != -float("inf") else 0


def main():
    test_list = [
        "abcabcbb",  # 3
        "bbbbb",  # 1
        "pwwkew",  # 3
    ]
    for s in test_list:
        res = Solution().lengthOfLongestSubstring(s)
        print(f"{res}")


if __name__ == "__main__":
    main()
