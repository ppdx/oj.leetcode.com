class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) < 2:
            return True

        step = 0
        cover = 0
        i = 0
        while i < len(A):
            if A[i]==0:
                return False
            if cover < A[i] + i:
                cover = A[i] + i
                step += 1
            if cover >= len(A) - 1:
                return True
            next = 0
            longest = 0
            j = i + 1
            while j <= i + A[i]:
                if A[j] + j > longest:
                    longest = A[j] + j
                    next = j
                j += 1
            i = next
        return True
