"""
    二维区域和检索 - 矩阵不可变
    给定一个二维矩阵 matrix，以下类型的多个请求：
    计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
"""

class NumMatrix:
    
    def __init__(self, matrix):
        self.matrix = matrix

        m = len(self.matrix)
        n = len(self.matrix[0])
        # presum专门记录以原点为顶点的矩阵的元素之和，就可以用几次加减运算算出任何一个子矩阵的元素和
        # 一般前缀和要是一维数组就在前面多个0，二维就多一圈。防止在计算的时候判断边界条件麻烦
        self.presum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.presum[i][j] = self.presum[i - 1][j] + self.presum[i][j - 1] - self.presum[i - 1][j - 1] + self.matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        return self.presum[row2 + 1][col2 + 1] - self.presum[row1][col2 + 1] - self.presum[row2 + 1][col1] + self.presum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
aaa = obj.sumRegion(1,2,2,4)
print(aaa)      # 12

# matrix                    # presum
# [[3,0,1,4,2],             # [[0, 0, 0, 0, 0, 0],
# [5,6,3,2,1],              # [0, 3, 3, 4, 8, 10],
# [1,2,0,1,5],              # [0, 8, 14, 18, 24, 27],
# [4,1,0,1,7],              # [0, 9, 17, 21, 28, 36],
# [1,0,3,0,5]]              # [0, 13, 22, 26, 34, 49],
#                           # [0, 14, 23, 30, 38, 58]]