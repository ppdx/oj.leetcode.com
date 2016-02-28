class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        l = 1
        elem = A[0]
        times = 1
        for i in range(1, len(A)):
            if elem == A[i]:
                if times == 1:
                    A[l] = A[i]
                    times += 1
                    l += 1
            else:
                times = 1
                elem = A[i]
                A[l] = A[i]
                l += 1
        return l

def test(*arg):
    for l in arg:
        print(l)
        print(Solution().removeDuplicates(l))

test([1, 1, 1, 2, 2, 3])