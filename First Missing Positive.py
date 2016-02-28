class Solution:
    # @param A, a list of integers
    # @return an integer

    def firstMissingPositive(self, A):
        if len(A) <= 0:
            return 1
        if len(A) == 1:
            if A[0] == 1:
                return 2
            else:
                return 1
        i = 0
        while i < len(A):
            if A[i] - 1 != i and A[i] <= len(A) and A[i] > 0 and A[i] != A[A[i] - 1]:
                j = A[i]
                A[i] = A[j - 1]
                A[j - 1] = j
            else:
                i += 1

        for i, n in enumerate(A):
            if n != i + 1:
                return i + 1
        return len(A) + 1


def test(*arg):
    for A in arg:
        print(A, Solution().firstMissingPositive(A))

test([1, 2, 0], [3, 4, -1, 1])
