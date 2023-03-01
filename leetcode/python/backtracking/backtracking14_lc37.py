

def solveSudoku(board):
    """
        解数独
        Do not return anything, modify board in-place instead.

        思路：
        二维递归：一个for循环遍历棋盘的行，一个for循环遍历棋盘的列，一行一列确定下来之后，递归遍历这个位置放9个数字的可能性！
    """

    def isValid(row, col, val, board):

        # 判断同一行是否冲突
        for i in range(9):
            if board[row][i] == str(val):
                return False
        
        # 判断同一列是否冲突
        for j in range(9):
            if board[j][col] == str(val):
                return False
        
        # 判断同一个九宫格是否冲突
        start_row = row // 3 * 3
        start_col = col // 3 * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        
        return True

    def backtracking(board):
        for i in range(len(board)):         # 遍历行
            for j in range(len(board[0])):  # 遍历列
                if board[i][j] != '.':      # 若空格内已有数字，跳过
                    continue
                for k in range(1, 10):
                    if isValid(i, j, k, board):
                        board[i][j] = str(k)
                        if backtracking(board):
                            return True
                        board[i][j] = '.'
                
                return False                # 若数字1-9都不能成功填入空格，返回False无解
        return True     # 有解

    backtracking(board)
    return board

aaa = solveSudoku([["5","3",".",".","7",".",".",".","."],
                    ["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],
                    ["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],
                    [".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]])

print(aaa)
