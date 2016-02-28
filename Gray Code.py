class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n==0:
            return [0]
        d=self.grayCode(n-1)
        t=2**(n-1)
        return d+[t+i for i in d[::-1]]

def test(*args):
    for i in args:
        print(i,Solution().grayCode(i))

test(*list(range(7)))
