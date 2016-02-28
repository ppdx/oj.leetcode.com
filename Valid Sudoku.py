class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        table = set()
        for i in range(0, 9):  # check column
            table.clear()
            for j in range(0, 9):
                c = board[i][j]
                if c == '.':
                    continue
                elif c in table:
                    return False
                else:
                    table.add(c)

        for j in range(0, 9):  # check row
            table.clear()
            for i in range(0, 9):
                c = board[i][j]
                if c == '.':
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
                        if c == '.':
                            continue
                        elif c in table:
                            return False
                        else:
                            table.add(c)
        return True

sudoku = ["....5..1.",
          ".4.3.....",
          ".....3..1",
          "8......2.",
          "..2.7....",
          ".15......",
          ".....2...",
          ".2.9.....",
          "..4......"]

print(Solution().isValidSudoku(sudoku))
