def spiralOrder(matrix):
    """
        螺旋矩阵
        给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
    """
    m = len(matrix)
    n = len(matrix[0])
    left = up = 0
    right = n - 1
    down = m - 1

    # 去看看参考链接，这个图画的很清楚
    result = []
    while len(result) < n * m:                  # 要遍历完整个数组
        if up <= down:                          # 在顶部，从左向右遍历
            for i in range(left, right + 1):
                result.append(matrix[up][i])
            up += 1                             # 上边界下移
        if left <= right:                       # 在右侧，从上向下遍历
            for j in range(up, down + 1):
                result.append(matrix[j][right])
            right -= 1                          # 右边界左移
        if up <= down:                          # 在底部，从右向左遍历
            for k in range(right, left - 1, -1):
                result.append(matrix[down][k])
            down -= 1                           # 下边界上移
        if left <= right:                       # 在左侧，从下向上遍历
            for l in range(down, up - 1, -1):
                result.append(matrix[l][left])
            left += 1                           # 左边界右移
    return result

    # left = 0
    # right = len(matrix[0]) - 1
    # up = 0
    # down = len(matrix) - 1
    # result = []
    # while left <= right and up <= down:
    #     for x in range(left, right + 1):
    #         result.append(matrix[up][x])
    #     for y in range(up + 1, down + 1):
    #         result.append(matrix[y][right])
    #     if left < right and up < down:
    #         for x in range(right - 1, left - 1, -1):
    #             result.append(matrix[down][x])
    #         for y in range(down - 1, up, -1):
    #             result.append(matrix[y][left])
    #     left += 1
    #     right -= 1
    #     up += 1
    #     down -= 1
    # return result

aaa = spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(aaa)      # [1, 2, 3, 6, 9, 8, 7, 4, 5]