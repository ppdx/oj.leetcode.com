class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n/2):
            for j in range((n+1)/2):
                tmp=matrix[j][n-i-1]
                matrix[j][n-i-1]=matrix[i][j]
                matrix[i][j]=matrix[n-j-1][i]
                matrix[n-j-1][i]=matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1]=tmp
        return matrix

matrix=[[1,2,3,4],
        [2,3,4,5],
        [5,6,7,8],
        [6,3,2,3]]
print(matrix)
Solution().rotate(matrix)
print(matrix)
