class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    def combinationSum2(self, candidates, target):
        if target <= 0:
            return []
        candidates.sort()

        ret = set()
        for i, n in enumerate(candidates):
            if target < n:
                break
            if i != 0 and candidates[i] == candidates[i - 1]:
                continue
            r = self.findTail(candidates, target - n, i + 1)
            if r is None:
                continue
            for l in r:
                ret.add((n,) + l)

        return [list(l) for l in ret]

    def findTail(self, candidates, target, i):
        if target < 0:
            return None
        elif target == 0:
            return [()]
        ret = []
        while i < len(candidates) and candidates[i] <= target:
            r = self.findTail(candidates, target - candidates[i], i + 1)
            if r is None:
                i += 1
                continue
            for l in r:
                ret.append((candidates[i],) + l)
            i += 1
        return ret if ret != [] else None


def test(*arg):
    for l, t in arg:
        print(l, t, Solution().combinationSum2(l, t))

test(([2, 2,2], 4))
