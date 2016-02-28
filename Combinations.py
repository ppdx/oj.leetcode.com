class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return self.generator(n, k, 0, 1)

    def generator(self, n, k, state, leval):
        if leval == k + 1:
            return [[]]
        res = []
        for i in range(state, n + leval - k):
            for l in self.generator(n, k, i + 1, leval + 1):
                res.append([i + 1] + l)
        return res

print((Solution().combine(4, 2)))