class Solution:
    # @param A, a list of integers
    # @return an integer

    def jump(self, A):
        if len(A) < 2:
            return 0

        step = 0
        cover = 0
        i = 0
        while i < len(A):
            if cover < A[i] + i:
                cover = A[i] + i
                step += 1
            if cover >= len(A) - 1:
                return step
            next = 0
            longest = 0
            j = i + 1
            while j <= i + A[i]:
                if A[j] + j > longest:
                    longest = A[j] + j
                    next = j
                j += 1
            i = next
        return step


def test(*arg):
    for l in arg:
        print(l, Solution().jump(l))

test([2, 3, 1, 1, 4], [1, 1, 1, 1])
