# https://leetcode.cn/problems/integer-to-roman/description

from typing import List


class Solution:
    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    def intToRoman(self, num: int) -> str:
        roman = list()
        for value, symbol in Solution.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)


def main():
    test_list = [
        3749, # "MMMDCCXLIX"
        58, # "LVIII"
        1994, # "MCMXCIV"
    ]
    for num in test_list:
        res = Solution().intToRoman(num)
        print(f"{res}")


if __name__ == '__main__':
    main()