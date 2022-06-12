
# BFS
# 还是很经典的
def orangeRotting(grid):
    """
        腐烂的橘子
    """
    row = len(grid)
    col = len(grid[0])
    if row == 1 and col == 1 and grid[0][0] != 1:
        return 0
    queue = []                      # 需要用一个队列, 队列里放坐标
    for i in range(row):            # 把腐烂的橘子的坐标先放到队列
        for j in range(col):
            if grid[i][j] == 2:
                queue.append((i, j))
    
    time = -1                       # 这个是特点, 去看看视频的解释
    while queue:                    # 然后开始弹, 一层一层弹
        current_len = len(queue)    # 找到当前层的个数
        for _ in range(current_len):
            i, j = queue.pop(0)
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:     # 上下左右的坐标
                temp_i = i + x
                temp_j = j + y
                # 判断点在不在grid的范围里, 然后是不是新鲜橘子
                if 0 <= temp_i and temp_i < row and 0 <= temp_j and temp_j < col and grid[temp_i][temp_j] == 1:
                    grid[temp_i][temp_j] = 2                # 是新鲜橘子的话, 就把它变成烂橘子
                    queue.append((temp_i, temp_j))          # 然后再添加倒队列中
        time += 1                   # 每次加一分钟

    for eachrow in grid:            # 判断有没有都腐烂完
        if 1 in eachrow:
            return -1
    return time

aaa = orangeRotting([[2,1,1],[1,1,0],[0,1,1]])
print(aaa)