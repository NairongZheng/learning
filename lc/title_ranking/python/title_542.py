# https://leetcode.cn/problems/01-matrix/description/


from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[-1 for _ in range(n)] for _ in range(m)] # 初始化全部填充特殊值 -1，代表未计算
        queue = []  # 初始化队列，把那些值为 0 的坐标放到队列里
        usage = set()   # 用是否 -1 来判断计算过没有也可以
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
                    usage.add((i, j))
        # 执行 BFS 算法框架，从值为 0 的坐标开始向四周扩散
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            i, j = queue.pop(0)
            for x, y in dirs:
                temp_i = i + x
                temp_j = j + y
                # 确保相邻的这个坐标没有越界且之前未被计算过
                if 0 <= temp_i < m and 0 <= temp_j < n and mat[temp_i][temp_j] == 1 and (temp_i, temp_j) not in usage:
                    result[temp_i][temp_j] = result[i][j] + 1
                    queue.append((temp_i, temp_j))
                    usage.add((temp_i, temp_j))
        return result


def main():
    test_list = [
        [[0,0,0],[0,1,0],[0,0,0]],  # [[0,0,0],[0,1,0],[0,0,0]]
        [[0,0,0],[0,1,0],[1,1,1]],  # [[0,0,0],[0,1,0],[1,2,1]]
    ]
    for mat in test_list:
        res = Solution().updateMatrix(mat)
        print(f"{res}")


if __name__ == "__main__":
    main()