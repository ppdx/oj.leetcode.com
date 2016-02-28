class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n==0:
            return []
        if n==1:
            return [[1]]
        matrix=[list(range(n)) for i in range(n)]
        cycle=(n+1)/2
        x=1
        for i in range(cycle):
            for c in range(i,n-i):
                matrix[i][c]=x
                x+=1
            for r in range(i+1,n-i):
                matrix[r][n-i-1]=x
                x+=1
            for c in range(n-i-2,i-1,-1):
                matrix[n-i-1][c]=x
                x+=1
            for r in range(n-i-2,i,-1):
                matrix[r][i]=x
                x+=1
        return matrix

print(Solution().generateMatrix(5))
