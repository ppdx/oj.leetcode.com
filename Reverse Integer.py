class Solution:
    # @return an integer
    def reverse(self, x):
        a = (int(("%s" % (abs(x)))[::-1])) * (1 if x > 0 else -1)
        return a if -1 * 2 ** 32 <= a <= 2 ** 32 - 1 else 0

if __name__ == '__main__':
    sol = Solution()
    print((sol.reverse(-123456789123)))
