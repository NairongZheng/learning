# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        win_len = len(needle)
        start = 0
        for end in range(win_len - 1, len(haystack)):
            if haystack[start : end + 1] == needle:
                return start
            start += 1
        return -1


def main():
    test_list = [
        ["sadbutsad", "sad"],  # 0
        ["leetcode", "leeto"],  # -1
    ]
    for haystack, needle in test_list:
        res = Solution().strStr(haystack, needle)
        print(f"{res}")


if __name__ == "__main__":
    main()
