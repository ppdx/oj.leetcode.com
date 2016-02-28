class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]

    def fourSum(self, num, target):
        num.sort()
        pairdata = { }
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                try:
                    pairdata[num[i] + num[j]].append((i, j))
                except Exception:
                    pairdata[num[i] + num[j]] = [(i, j)]

        res = set()
        for key, valuea in pairdata.items():
            try:
                valueb = pairdata[target - key]
                for a in valuea:
                    for b in valueb:
                        if a!=b and a[1] < b[0]:
                            res.add((num[a[0]], num[a[1]], num[b[0]], num[b[1]]))
            except Exception:
                pass

        return [list(i) for i in res]

def test(*pairs):
    for a, t in pairs:
        print(a, t, Solution().fourSum(a, t))

test(([1, 0, -1, 0, -2, 2], 0))
