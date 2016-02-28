class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        num = [1, 2]
        for i in range(2, n):
            num.append(num[-1] + num[-2])
        return num[n - 1]

print((Solution().climbStairs(5)))
