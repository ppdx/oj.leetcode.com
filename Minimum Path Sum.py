class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        n=len(grid)
        m=len(grid[0])
        for i in range(1,m):
            grid[0][i]+=grid[0][i-1]
        for i in range(1,n):
            grid[i][0]+=grid[i-1][0]
        for i in range(1,min(m,n)):
            for j in range(i,m):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
            for j in range(i+1,n):
                grid[j][i]+=min(grid[j][i-1],grid[j-1][i])
        return grid[-1][-1]

print(Solution().minPathSum([[1,2,3],[1,2,3],[1,2,3]]))
