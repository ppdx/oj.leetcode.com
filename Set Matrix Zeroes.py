class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        for elem in matrix[0]:
            if elem == 0:
                line0 = True
                break
        else:
            line0 = False

        for i in range(n):
            if matrix[i][0] == 0:
                column0 = True
                break
        else:
            column0 = False

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if line0:
            for i in range(m):
                matrix[0][i] = 0

        if column0:
            for i in range(n):
                matrix[i][0] = 0

print(Solution().setZeroes([[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))