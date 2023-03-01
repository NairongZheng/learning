

# DFS
def maxAreaOfIsland(grid):
    """
        岛屿的最大面积
    """
    def dfs(grid, i, j):
        if 0 <= i < row and 0 <= j < col and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j - 1)
        else:
            return 0
    row = len(grid)
    col = len(grid[0])
    total_result = 0
    for i in range(row):
        for j in range(col):
            total_result = max(total_result, dfs(grid, i, j))
    return total_result

aaa = maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])

print(aaa)