def floodFill(image, sr, sc, color):
    
    m = len(image)
    n = len(image[0])

    stack = [(sr, sc)]
    target = image[sr][sc]
    while stack:
        n = len(stack)
        for _ in range(n):
            cur_i, cur_j = stack.pop(0)
            image[cur_i][cur_j] = color
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                temp_i = cur_i + x
                temp_j = cur_j + y
                if 0 <= temp_i < m and 0 <= temp_j < n and image[temp_i][temp_j] == target:
                    image[temp_i][temp_j] = color
                    stack.append((temp_i, temp_j))
    return image

aaa = floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(aaa)