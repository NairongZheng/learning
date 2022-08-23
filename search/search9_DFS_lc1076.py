
"""
    球会落何处
"""

class Solution:
    def findBall(self, grid):
        result = []
        m = len(grid)
        n = len(grid[0])
        for col in range(n):
            result.append(self.dfs(grid, 0, col))
        return result
    
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if grid[i][j] == 1 and j == n - 1:              # 第 1 种情况：到达最右端，卡住
            return -1
        if grid[i][j] == -1 and j == 0:                 # 第 2 种情况：到达最左端，卡住
            return -1
        if grid[i][j] != grid[i][j + grid[i][j]]:       # 第 3、4 种情况：形成 V 型，无法下落
            return -1
        if i == m - 1:                                  # 第 6 种情况：到达最后一行，需要继续下落
            return j + grid[i][j]
        return self.dfs(grid, i + 1, j + grid[i][j])    # 第 5 种情况：未到达最后一行，继续下落

aaa = Solution()
bbb = aaa.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
print(bbb)      # [1, -1, -1, -1, -1]