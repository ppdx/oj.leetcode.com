class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    # @profile
    def maximalRectangle(self, matrix):
        row_num = len(matrix)
        if row_num == 0:
            return 0
        column_num = len(matrix[0])
        dp = []
        res = 0
        for row in matrix:
            line=[0]*column_num
            line[-1] = 1 if row[-1] == '1' else 0
            for j in range(column_num-2,-1,-1):
                if row[j] == '1':
                    line[j] = line[j + 1] + 1
            dp.append(line)

        for i in range(row_num):
            for j in range(column_num):
                if (column_num - j) * (row_num - i) <= res:
                    break
                width = dp[i][j]
                k = i
                while k < row_num and width > 0:
                    if width * (row_num - i) < res:
                        break
                    if width > dp[k][j]:
                        width = dp[k][j]
                    res = max(res, width * (k - i + 1))
                    k += 1
        return res


def printMatrixs(matrix):
    for row in matrix:
        print('|', end=' ')
        for ceil in row:
            print(ceil, end=' ')
        print('|')


def test(*matrixs):
    for m in matrixs:
        printMatrixs(m)
        print(Solution().maximalRectangle(m))

test(["111100", "111011", "101011", "011111", "111111"])
