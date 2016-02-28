class Solution:
    # @param A, a list of integers
    # @return an integer

    def trap(self, A):
        if len(A) < 3:
            return 0
        total_v = 0
        i = 0
        while i < len(A):
            if A[i] == 0:
                i += 1
                continue
            v = 0
            left = i + 1
            while left < len(A):
                if A[i] > A[left]:
                    v += A[i] - A[left]
                else:
                    total_v += v
                    i = left
                    break
                left += 1
            else:
                break
        j = len(A) - 1
        while j > i:
            if A[j] == 0:
                j -= 1
                continue
            v = 0
            right = j - 1
            while j >= i:
                if A[j] > A[right]:
                    v += A[j] - A[right]
                else:
                    total_v += v
                    j = right
                    break
                right -= 1
            else:
                break

        return total_v


def test(*arg):
    for l in arg:
        print(l, Solution().trap(l))

test([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [4, 2, 3])
