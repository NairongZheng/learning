# https://leetcode.cn/problems/candy/description

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1 for _ in range(n)] # 每个人至少分一个
        # 先确定右边评分大于左边的情况
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1
        # 再确定左边评分大于右边的情况
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i], result[i + 1] + 1)
        return sum(result)


def main():
    test_list = [
        [1,0,2], # 5
        [1,2,2], # 4
        [1, 5, 6, 4, 3, 4] # 11
    ]
    for ratings in test_list:
        res = Solution().candy(ratings)
        print(f"{res}")


if __name__ == '__main__':
    main()