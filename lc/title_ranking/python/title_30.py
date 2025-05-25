# https://leetcode.cn/problems/substring-with-concatenation-of-all-words/description

from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        words_mum = len(words)
        word_len = len(words[0])
        total_len = words_mum * word_len
        s_len = len(s)
        if s_len < total_len:
            return res
        words_dict = Counter(words)
        # 外层循环控制起始偏移量，范围是0-word_len-1
        for offset in range(word_len):
            left = offset
            cur_dict = Counter()
            count = 0
            # 内层循环处理每个可能的窗口
            for right in range(offset, s_len - word_len + 1, word_len):
                cur_word = s[right : right + word_len]
                # 如果当前单词不在words中，重置窗口
                if cur_word not in words_dict:
                    cur_dict = Counter()
                    count = 0
                    left = right + word_len
                else:
                    # 增加当前单词计数
                    cur_dict[cur_word] += 1
                    count += 1
                    while cur_dict[cur_word] > words_dict[cur_word]:
                        left_word = s[left : left + word_len]
                        cur_dict[left_word] -= 1
                        count -= 1
                        left += word_len
                    if count == words_mum:
                        res.append(left)
                        left_word = s[left : left + word_len]
                        cur_dict[left_word] -= 1
                        count -= 1
                        left += word_len
        return res

    def myCode(self, s, words):
        """暴力解法，会有一个用例超时"""
        res = []
        words_num = len(words)
        word_len = len(words[0])
        total_len = words_num * word_len
        words_dict = Counter(words)
        if total_len > len(s):
            return res
        big_window_len = total_len
        small_window_len = word_len
        idx = 0
        while idx < len(s) - big_window_len + 1:
            flag = True
            jdx = idx
            words_dict = Counter(words)
            while jdx < idx + big_window_len - small_window_len + 1:
                cur_word = s[jdx : jdx + word_len]
                if cur_word in words_dict and words_dict[cur_word] != 0:
                    jdx += word_len
                    words_dict[cur_word] -= 1
                else:
                    flag = False
                    break
            if flag:
                res.append(idx)
                idx += 1
            else:
                idx += 1
        return res


def main():
    test_list = [
        # ["barfoothefoobarman", ["foo", "bar"]],  # [0,9]
        # ["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]],  # []
        ["barfoofoobarthefoobarman", ["bar", "foo", "the"]],  # [6,9,12]
        # ["aaa", ["a", "a"]],  # [0, 1]
    ]
    for s, words in test_list:
        res = Solution().findSubstring(s, words)
        print(f"{res}")


if __name__ == "__main__":
    main()
