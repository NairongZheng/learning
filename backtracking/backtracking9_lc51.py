

def solveNQueens(n):
    """
        N皇后
        n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
        每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
    """

    board = [['.'] * n for _ in range(n)]
    result = []

    def isVaild(board, row, col):

        # 判断同一列是否冲突
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        
        # 判断左上角是否冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # 判断右上角是否冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtracking(board, row, n):
        if row == n:
            temp_result = []
            for temp in board:
                temp_str = ''.join(temp)
                temp_result.append(temp_str)
            result.append(temp_result)
        
        for col in range(0, n):
            if not isVaild(board, row, col):
                continue
            board[row][col] = 'Q'
            backtracking(board, row + 1, n)
            board[row][col] = '.'
    
    backtracking(board, 0, n)
    return result

aaa = solveNQueens(4)
print(aaa)