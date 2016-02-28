class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer

    def findSubstring(self, S, L):
        data = { }
        for s in L:
            try:
                data[s] += 1
            except Exception:
                data[s] = 1

        res = []
        length = len(L[0])
        size = len(L)
        for i in range(len(S) - length + 1):
            tmpdata = {}
            s = S[i:i + length * size]
            for j in range(size):
                try:
                    tmpdata[s[j * length:(j + 1) * length]] += 1
                except Exception:
                    tmpdata[s[j * length:(j + 1) * length]]=1
            if tmpdata==data:
                res.append(i)
        return res

def test(*pairs):
    for s, l in pairs:
        print(s, l, Solution().findSubstring(s, l))

test(("barfoothefoobarman", ["foo", "bar"]))
