

# BFS
def maxAreaOfIsland(grid):
    """
        岛屿的最大面积
    """
    row = len(grid)
    col = len(grid[0])
    total_result = 0
    for i in range(row):
        for j in range(col):
            result = 0
            queue = []
            if grid[i][j] == 1:
                result += 1
                grid[i][j] = 0
                queue.append((i, j))
                while queue:
                    cur_i, cur_j = queue.pop(0)
                    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        temp_i = cur_i + x
                        temp_j = cur_j + y
                        if 0 <= temp_i < row and 0 <= temp_j < col and grid[temp_i][temp_j]:
                            grid[temp_i][temp_j] = 0
                            result += 1
                            queue.append((temp_i, temp_j))
            total_result = max(total_result, result)
    return total_result

aaa = maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])

print(aaa)