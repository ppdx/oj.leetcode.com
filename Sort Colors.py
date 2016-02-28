class Solution:
    # @param A a list of integers
    # @return nothing, sort in place

    def sortColors(self, A):
        l = [0, 0, 0]
        for i in A:
            l[i] += 1
        x = 0
        for i, n in enumerate(l):
            for j in range(0, n):
                A[x] = i
                x += 1


def test(A):
    print(A, ' => ', end=' ')
    Solution().sortColors(A)
    print(A)

test([0, 0, 2, 1, 1, ])
