class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        int_board = self.toint(board)
        emptyceil = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    emptyceil.append((i, j))

        stack = []
        x = -1
        while True:
            if self.isValidSudoku(int_board):
                if self.isfull(int_board):
                    break
                x += 1
                i, j = emptyceil[x]
                stack.append(1)
                int_board[i][j] = 1
            else:
                while stack[-1] == 9:
                    stack.pop()
                    i, j = emptyceil[x]
                    int_board[i][j] = -1
                    x -= 1
                stack[-1] += 1
                i, j = emptyceil[x]
                int_board[i][j] += 1

        for i in range(9):
            for j in range(9):
                board[i][j] = str(int_board[i][j])

    def toint(self, board):
        b = []
        for row in board:
            r = []
            for ceil in row:
                if ceil != '.':
                    r.append(int(ceil))
                else:
                    r.append(-1)
            b.append(r)
        return b

    def isfull(self, board):
        for row in board:
            try:
                row.index(-1)
                return False
            except Exception:
                pass
        return True

    def isValidSudoku(self, board):
        table = set()
        for i in range(0, 9):  # check column
            table.clear()
            for j in range(0, 9):
                c = board[i][j]
                if c == -1:
                    continue
                elif c in table:
                    return False
                else:
                    table.add(c)

        for j in range(0, 9):  # check row
            table.clear()
            for i in range(0, 9):
                c = board[i][j]
                if c == -1:
                    continue
                elif c in table:
                    return False
                else:
                    table.add(c)

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                table.clear()
                for i in range(0, 3):
                    for j in range(0, 3):
                        c = board[x + i][y + j]
                        if c == -1:
                            continue
                        elif c in table:
                            return False
                        else:
                            table.add(c)
        return True

    def checkCeil(self,board,row,column):
        rowTable=set()
        columnTable=set()
        squareTable=set()
        for i in range(9):
            c=board[row][i]
            if c==-1:
                continue
            elif c in rowTable:
                return False
            else:
                rowTable.add(c)

            c=board[i][column]
            if c==-1:
                continue
            elif c in columnTable:
                return False
            else:
                columnTable.add(c)

            c=board[(row/3)*3+(i%3)][(column/3)*3+(i/3)]
            if c==-1:
                continue
            elif c in squareTable:
                return False
            else:
                squareTable.add(c)




def print_board(board):
    for row in board:
        for ceil in row:
            print(ceil, end=' ')
        print()
    print()

board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

print_board(board)
Solution().solveSudoku(board)
print_board(board)
