class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer

    def subsetsWithDup(self, S):
        res = set()
        S.sort()
        for i in range(len(S) + 1):
            for l in self.generator(S, i, 0, 1):
                res.add(l)
        return [list(l) for l in res]

    def generator(self, S, k, state, leval):
        if leval == k + 1:
            return [()]
        res = []
        for i in range(state, len(S) + leval - k):
            for l in self.generator(S, k, i + 1, leval + 1):
                res.append((S[i],) + l)
        return res

print((Solution().subsetsWithDup([1, 2, 2])))
