class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        num = 0
        while n > 0:
            n = n // 5
            num += n
        return num

for i in range(1, 11):
    print(("%d : %d" % (i, Solution().trailingZeroes(i))))

