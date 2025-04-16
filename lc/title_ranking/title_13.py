# https://leetcode.cn/problems/roman-to-integer/description

from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        map_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # 优美解：当前位置的元素比下个位置的元素小，就减去当前值，否则加上当前值
        res = 0
        for i in range(len(s)):
            cur_val = map_dict[s[i]]
            if i < len(s) - 1 and cur_val < map_dict[s[i + 1]]:
                res -= cur_val
            else:
                res += cur_val
        return res

        # # 暴力解
        # res = 0
        # res += map_dict[s[0]]
        # for i in range(1, len(s)):
        #     cur_str = s[i]
        #     cur_val = map_dict[cur_str]
        #     res += cur_val
        #     pre_str = s[i - 1]
        #     pre_val = map_dict[pre_str]
        #     if pre_val == 1 and cur_val in [5, 10]:
        #         res -= 2 * pre_val
        #     if pre_val == 10 and cur_val in [50, 100]:
        #         res -= 2 * pre_val
        #     if pre_val == 100 and cur_val in [500, 1000]:
        #         res -= 2 * pre_val
        # return res


def main():
    test_list = [
        "III", # 3
        "IV", # 4
        "LVIII", # 58
        "MCMXCIV", # 1994
    ]
    for s in test_list:
        res = Solution().romanToInt(s)
        print(f"{res}")


if __name__ == '__main__':
    main()