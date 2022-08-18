
def rotate_clockwise(matrix):
    """
        Do not return anything, modify matrix in-place instead.

        旋转图像
        给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
        你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

        思路：
        走不寻常的路，用常规的方法去推ij怎么变什么关系，比较复杂，可以用点灵活的方法，镜像、翻转之类的
        这种题要仔细观察
    """
    n = len(matrix)
    # 先沿对角线镜像对称矩阵
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 再左右翻转
    for row in matrix:
        left = 0
        right = len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
    return matrix

def rotate_anticlockwise(matrix):
    n = len(matrix)
    # 沿左下到右上的对角线镜像对称二维矩阵
    for i in range(n):
        for j in range(n - i):
            matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
    # 再左右翻转
    for row in matrix:
        left = 0
        right = len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
    return matrix

aaa = rotate_clockwise([[1,2,3],[4,5,6],[7,8,9]])
bbb = rotate_anticlockwise([[1,2,3],[4,5,6],[7,8,9]])

print(aaa)          # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(bbb)          # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]