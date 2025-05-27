# https://leetcode.cn/problems/longest-palindromic-substring/description


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)
            if len(result) < len(s1):
                result = s1
            if len(result) < len(s2):
                result = s2
        return result

    def palindrome(self, s, left, right):
        """返回以 s[left] 和 s[right] 为中心的最长回文串"""
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left + 1 : right]


def main():
    test_list = [
        "babad",  # bab
        "cbbd",  # bb
    ]
    for s in test_list:
        res = Solution().longestPalindrome(s)
        print(f"{res}")


if __name__ == "__main__":
    main()
