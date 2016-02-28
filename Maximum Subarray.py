class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A)==0:
            return 0
        if len(A)==1:
            return A[0]
        large = 0
        current = 0
        for n in A:
            current += n
            if current > large:
                large = current
            elif current < 0:
                current = 0
        if large==0:
            large=max(A)
        return large

print(Solution().maxSubArray([-2,-3,-1,-5]))
