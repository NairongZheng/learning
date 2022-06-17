class Solution:
    def updateMatrix(self, mat):
        row = len(mat)
        col = len(mat[0])
        result = [[0 for i in range(col)] for j in range(row)]
        queue = []
        usage = set()           # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX算过了的就不要再算了
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    usage.add((i, j))
        while queue:
            i, j = queue.pop(0)
            for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
                temp_i = i + x
                temp_j = j + y
                if 0 <= temp_i < row and 0 <= temp_j < col and mat[temp_i][temp_j] == 1 and (temp_i, temp_j) not in usage:
                    result[temp_i][temp_j] = result[i][j] + 1
                    queue.append((temp_i, temp_j))
                    usage.add((temp_i, temp_j))
        return result

aaa = Solution()
bbb = aaa.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
print(bbb)