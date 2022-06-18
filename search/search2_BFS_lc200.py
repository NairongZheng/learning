
# BFS
def numIslands(grid):
    """
        岛屿的数量
        注意跟994的区别
    """
    row = len(grid)
    if row == 0:
        return 0
    col = len(grid[0])
    if col == 0:
        return 0

    queue = []
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                grid[i][j] = '0'        # 找到岛屿就把他变成水
                queue.append((i, j))    # 然后再把以他周围的岛屿都变成水
                while queue:
                    cur_i, cur_j = queue.pop(0)
                    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        temp_i = cur_i + x
                        temp_j = cur_j + y
                        if 0 <= temp_i < row and 0 <= temp_j < col and grid[temp_i][temp_j] == '1':
                            grid[temp_i][temp_j] = '0'
                            queue.append((temp_i, temp_j))
                count += 1
    return count

aaa = numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])

print(aaa)