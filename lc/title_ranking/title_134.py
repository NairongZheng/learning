# https://leetcode.cn/problems/gas-station/description

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 只需要考虑总油量和当前油量，如果gas的总油量小于cost的总油量，则一定无法绕一周，反之一定有一种方案可以绕一周。
        # 因此可不断计算当前油量，如果当前油量小于0，则证明当前的起点无法完成绕一周，需要更换为当前失败的起点的下一个点继续计算。
        if sum(gas) < sum(cost):
            return -1
        start = 0
        cur_sum = 0
        for i in range(len(gas)):
            cur_sum = cur_sum + gas[i] - cost[i]
            if cur_sum < 0:     # 当前的起点无法完成绕一周
                start = i + 1   # 更换为当前失败的起点的下一个点继续计算
                cur_sum = 0
        return start
        

def main():
    test_list = [
        [[1,2,3,4,5], [3,4,5,1,2]], # 3
        [[2,3,4], [3,4,3]], # -1
    ]
    for gas, cost in test_list:
        res = Solution().canCompleteCircuit(gas, cost)
        print(f"{res}")


if __name__ == '__main__':
    main()