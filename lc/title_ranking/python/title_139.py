# https://leetcode.cn/problems/word-break/description

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]  # 表示字符串前i个字符组成的字符串s[0:i]能否被空格拆分成若干个字典中出现的单词。
        dp[0] = True # 定义 dp[0]=true 表示空串且合法。
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDictSet):  # dp[i]=dp[j] && check(s[j:i])
                    dp[i] = True
                    break
        return dp[-1]


def main():
    test_list = [
        ["leetcode", ["leet", "code"]],  # true
        ["applepenapple", ["apple", "pen"]],  # true
        ["catsandog", ["cats", "dog", "sand", "and", "cat"]],  # false
    ]
    for s, wordDict in test_list:
        res = Solution().wordBreak(s, wordDict)
        print(f"{res}")


if __name__ == "__main__":
    main()
