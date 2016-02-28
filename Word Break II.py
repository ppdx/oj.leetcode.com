class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return [""]
        if len(dict) == 0:
            return []
        if not self.canBreak(s, dict):
            return []

        maxWordLength = len(max(list(dict), key=len))
        minWordLength = len(min(list(dict), key=len))
        length = len(s)
        res = []
        stack = [(0, [])]
        while len(stack):
            i, head = stack.pop()
            a = i + maxWordLength + 1
            b = i + minWordLength
            for j in range(b, min(a, length) + 1):
                subStr = s[i:j]
                if subStr in dict:
                    if j == length:
                        res.append(" ".join(head + [subStr]))
                    else:
                        stack.append((j, head + [subStr]))
        return res

    def canBreak(self, s, dict):
        maxWordLength = len(max(list(dict), key=len))
        stack = [0]
        mark = [False] * (len(s) + 1)
        while len(stack) != 0:
            i = stack.pop()
            mark[i] = True
            for j in range(min(maxWordLength + 1, len(s) - i + 1)):
                if not mark[i + j] and s[i: i + j] in dict:
                    if i + j == len(s):
                        return True
                    stack.append(i + j)
        return mark[-1]


def test():
    args = [("catsanddog", {"cat", "cats", "and", "sand", "dog"})]
    for arg in args:
        print(Solution().wordBreak(*arg))


if __name__ == '__main__':
    from timeit import Timer

    t1 = Timer(test, "from __main__ import test")
    print(t1.timeit(1))