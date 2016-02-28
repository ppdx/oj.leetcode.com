class Solution:
    # @return a string

    def getPermutation(self, n, k):
        nums = [str(i + 1) for i in range(n)]
        factorial = self.factorial(n)
        res = []
        for i in range(0, n):
            index = (k - 1) / factorial[-i - 1]
            res.append(nums[index])
            k %= factorial[n - i - 1]
            del nums[index]
        return ''.join(res)

    def factorial(self, n):
        result = [1, 1]
        for i in range(2, n):
            result.append(result[i - 1] * i)
        return result

n = 5
for i in range(1, 20):
    print(Solution().getPermutation(n, i))
