# https://leetcode.cn/problems/zigzag-conversion/description


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res_list = [[] for _ in range(numRows)]
        row_idx = 0
        tag = -1
        for i in range(len(s)):
            res_list[row_idx].append(s[i])
            if row_idx == 0 or row_idx == numRows - 1:
                tag *= -1
            row_idx += tag
        res_str = ""
        for i in range(numRows):
            for j in range(len(res_list[i])):
                res_str += res_list[i][j]
        return res_str


def main():
    test_list = [
        ["PAYPALISHIRING", 3],  # PAHNAPLSIIGYIR
        ["PAYPALISHIRING", 4],  # PINALSIGYAHRPI
    ]
    for s, numRows in test_list:
        res = Solution().convert(s, numRows)
        print(f"{res}")


if __name__ == "__main__":
    main()
