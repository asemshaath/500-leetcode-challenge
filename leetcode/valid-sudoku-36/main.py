class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows

        for i in range(len(board)):
            row_set = set()
            for j in range(len(board[0])):
                if board[i][j] in row_set and board[i][j] != '.':
                    return False
                else:
                    row_set.add(board[i][j])
        print('row checked')

        for i in range(len(board)):
            col_set = set()
            for j in range(len(board[0])):
                if board[j][i] in col_set and board[j][i] != '.':
                    return False
                else:
                    col_set.add(board[j][i])
        
        print('col checked')        
        # 0 1 2  3 4 5  6 7 8
        # 0 3 6
        
 
        
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                r = i // 3
                c = j // 3
                # square_indx = r + c

                if board[i][j] in squares[r][c] and board[i][j] != '.':
                    return False
                else:
                    squares[r][c].add(board[i][j])

        print('suqares checked')
        return True
