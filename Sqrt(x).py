class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x<2:
            return x
        y=x/2.0
        last=0.0
        while abs(last-y)>0.5:
            last=y
            y=(y+x/y)/2
        return int(y)

sol=Solution()
for i,n in enumerate([sol.sqrt(x) for x in range(50)]):
    print(i,n)