"""
    螺旋矩阵 II
    给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""

def generateMatrix(n):

    # 也是参考链接的写法
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    up = 0
    down = n - 1
    left = 0
    right = n - 1
    num = 1     # 要填入的数字
    while num <= n * n:
        if up <= down:                              # 在顶部，从左向右遍历
            for i in range(left, right + 1):
                matrix[up][i] = num
                num += 1
            up += 1                                 # 上边界下移
        if left <= right:                           # 在右侧，从上向下遍历
            for i in range(up, down + 1):
                matrix[i][right] = num
                num += 1
            right -= 1                              # 右边界左移
        if up <= down:                              # 在底部，从右向左遍历
            for i in range(right, left - 1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1                               # 下边界上移
        if left <= right:                           # 在左侧，从下向上遍历
            for i in range(down, up - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1                               # 左边界右移
    return matrix

    # matrix = [[0 for _ in range(n)] for _ in range(n)]
    # left = 0
    # right = n - 1
    # up = 0
    # down = n - 1
    # number = 1
    # while left < right and up < down:
    #     for x in range(left, right):
    #         matrix[up][x] = number
    #         number += 1
    #     for y in range(up, down):
    #         matrix[y][right] = number
    #         number += 1
    #     for x in range(right, left, -1):
    #         matrix[down][x] = number
    #         number += 1
    #     for y in range(down, up, -1):
    #         matrix[y][left] = number
    #         number += 1
    #     up += 1
    #     right -= 1
    #     down -= 1
    #     left += 1
    # if n % 2:
    #     matrix[n // 2][n // 2] = number
    # return matrix

aaa = generateMatrix(3)
print(aaa)      # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]