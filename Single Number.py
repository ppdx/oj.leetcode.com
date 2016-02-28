class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for n in A:
            res ^= n
        return res


def test():
    A = [1, 1, 2]
    print(Solution().singleNumber(A))


test()