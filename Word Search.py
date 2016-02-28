class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if word == '':
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = '!'
                    if self.find(board, word[1:], i, j):
                        return True
                    board[i][j] = word[0]
        return False

    def find(self, board, word, i, j):
        if word == '':
            return True
        if i > 0 and board[i - 1][j] == word[0]:
            board[i - 1][j] = '!'
            if self.find(board, word[1:], i - 1, j):
                return True
            board[i - 1][j] = word[0]

        if i < len(board) - 1 and board[i + 1][j] == word[0]:
            board[i + 1][j] = '!'
            if self.find(board, word[1:], i + 1, j):
                return True
            board[i + 1][j] = word[0]

        if j > 0 and board[i][j - 1] == word[0]:
            board[i][j - 1] = '!'
            if self.find(board, word[1:], i, j - 1):
                return True
            board[i][j - 1] = word[0]

        if j < len(board[0]) - 1 and board[i][j + 1] == word[0]:
            board[i][j + 1] = '!'
            if self.find(board, word[1:], i, j + 1):
                return True
            board[i][j + 1] = word[0]

        return False

def test(*arg):
    for a in arg:
        print(a)
        print(Solution().exist(*a))

test(([list("ABCE"), list("SFCS"), list("ADEE")], "ABCB"))
