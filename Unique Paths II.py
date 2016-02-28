class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer

    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        full = 1
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
                full = 0
            else:
                obstacleGrid[0][i] = full
        full = obstacleGrid[0][0]
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
                full = 0
            else:
                obstacleGrid[i][0] = full
        for i in range(1, min(m, n)):
            for j in range(i, m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[
                        i - 1][j] + obstacleGrid[i][j - 1]
            for j in range(i + 1, n):
                if obstacleGrid[j][i] == 1:
                    obstacleGrid[j][i] = 0
                else:
                    obstacleGrid[j][i] = obstacleGrid[j][
                        i - 1] + obstacleGrid[j - 1][i]
        return obstacleGrid[-1][-1]

print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0] ]))
print(Solution().uniquePathsWithObstacles([[1],[0]]))
