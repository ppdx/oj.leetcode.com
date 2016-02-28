class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix)==0:
            return []
        if len(matrix)==1:
            return matrix[0]
        n=len(matrix)
        m=len(matrix[0])
        cycle=(n+1)/2 if m>n else (m+1)/2
        ret=[]
        a,b=n,m
        for i in range(cycle):
            for c in range(i,m-i):
                ret.append(matrix[i][c])
            for r in range(i+1,n-i):
                ret.append(matrix[r][m-i-1])
            if a==1 or b==1:
                break
            for c in range(m-i-2,i-1,-1):
                ret.append(matrix[n-i-1][c])
            for r in range(n-i-2,i,-1):
                ret.append(matrix[r][i])
            a-=2
            b-=2
        return ret

def test(*arg):
    for ll in arg:
        print(ll)
        print(Solution().spiralOrder(ll))
        print()
test([ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]],[[1]],[[1,2],[3,4]],[[3],[2]],
     [[7],[9],[6]],[[2,5],[8,4],[0,-1]])
