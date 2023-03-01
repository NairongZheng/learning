

def exist(board, word):
    """
        单词搜索
        给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
        单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
    """
    row = len(board)
    col = len(board[0])

    def dfs(cur_i, cur_j, index):
        if board[cur_i][cur_j] != word[index]:
            return False
        if index == len(word) - 1:
            return True
        board[cur_i][cur_j] = '#'
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:     # 分别搜索上下左右
            temp_i = cur_i + x
            temp_j = cur_j + y
            if 0 <= temp_i < row and 0 <= temp_j < col and dfs(temp_i, temp_j, index + 1):  # 上下左右有满足的话就进去继续搜索下一个字母
                return True
        board[cur_i][cur_j] = word[index]       # 没有满足的话就把#号撤销（回溯）
    
    for i in range(row):
        for j in range(col):
            if dfs(i, j, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
aaa = exist(board, word)
print(aaa)      