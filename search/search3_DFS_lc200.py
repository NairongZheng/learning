

# DFS
def numIslands(grid):
    """
        岛屿的数量
    """
    def dfs(grid, i, j):
        """
            dfs
        """
        if 0 <= i < row and 0 <= j < col and grid[i][j] == '1':
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)


    if not grid:
        return 0
    row = len(grid)
    col = len(grid[0])
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

aaa = numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])

print(aaa)