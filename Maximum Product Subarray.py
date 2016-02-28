class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        max_global = max_local = min_local = A[0]
        for a in A[1:]:
            x = [a, max_local * a, min_local * a]
            max_local = max(x)
            min_local = min(x)
            max_global = max(max_local, max_global)
        return max_global

def tests(*A):
    for a in A:
        print(a,Solution().maxProduct(a))

tests([2,3,-2,4])
