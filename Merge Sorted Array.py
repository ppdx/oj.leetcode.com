class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing

    def merge(self, A, m, B, n):
        l = m + n - 1
        m -= 1
        n -= 1
        while l >= 0:
            if n == -1:
                return
            elif m == -1:
                A[:n + 1] = B[:n + 1]
                return
            if A[m] > B[n]:
                A[l] = A[m]
                m -= 1
            else:
                A[l] = B[n]
                n -= 1
            l -= 1
