class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    def combinationSum(self, candidates, target):
        if target <= 0:
            return []
        candidates.sort()

        ret = []
        for i, n in enumerate(candidates):
            if target < n:
                break
            r = self.findTail(candidates, target - n, i)
            if r is None:
                continue
            for l in r:
                ret.append([n] + l)

        return ret

    def findTail(self, candidates, target, i):
        if target < 0:
            return None
        elif target == 0:
            return [[]]
        ret = []
        while i < len(candidates) and candidates[i] <= target:
            r = self.findTail(candidates, target - candidates[i], i)
            if r is None:
                i += 1
                continue
            for l in r:
                ret.append([candidates[i]] + l)
            i += 1
        return ret if ret !=[] else None

def test(*arg):
    for l, t in arg:
        print(l, t, Solution().combinationSum(l, t))

test(([2, 3, 6, 7], 7))
