class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        world=[list(range(m)) for i in range(n)]
        for i in range(m):
            world[0][i]=1
        for i in range(n):
            world[i][0]=1
        for i in range(1,min(m,n)):
            for j in range(i,m):
                world[i][j]=world[i-1][j]+world[i][j-1]
            for j in range(i+1,n):
                world[j][i]=world[j][i-1]+world[j-1][i]
        return world[-1][-1]

def test(*arg):
    for m,n in arg:
        print(m,n,Solution().uniquePaths(m,n))

test((1,2),(2,3))
