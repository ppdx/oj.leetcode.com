class Solution:
    # @return a string

    def minWindow(self, S, T):
        src = [0] * 256
        found = [0] * 256
        for c in T:
            src[ord(c)] += 1

        numFound = 0
        winStart, winEnd = -1, len(S)
        i = start = 0
        queue = []
        while i < len(S):
            c = ord(S[i])
            if src[c] != 0:
                queue.append(i)
                found[c] += 1
                if found[c] <= src[c]:
                    numFound += 1
                if numFound == len(T):
                    while True:
                        k = queue.pop(0)
                        c = ord(S[k])
                        found[c] -= 1
                        if src[c] > found[c]:
                            break
                    if winEnd - winStart > i - k:
                        winStart = k
                        winEnd = i
                    numFound -= 1
            i += 1
        return '' if winStart == -1 else S[winStart:winEnd + 1]


def test(*args):
    for p in args:
        print(p)
        print(Solution().minWindow(*p))


test(("ADOBECODEBANC", "ABC"))
