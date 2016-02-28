class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        res=[]
        S.sort()
        for i in range(len(S)+1):
            res.extend(self.generator(S,i,0,1))
        return res

    def generator(self, S, k, state, leval):
        if leval == k + 1:
            return [[]]
        res = []
        for i in range(state, len(S) + leval - k):
            for l in self.generator(S, k, i + 1, leval + 1):
                res.append([S[i]] + l)
        return res

print((Solution().subsets([4,1,0])))