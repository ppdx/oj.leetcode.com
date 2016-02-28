class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak(self, s, dict):
        if s == "":
            return True
        if len(dict) == 0:
            return False
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
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    dict = {"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"}
    # print Solution().wordBreak(s, dict)
    Solution().wordBreak(s, dict)


if __name__ == '__main__':
    from timeit import Timer
    t1 = Timer(test, "from __main__ import test")
    print(t1.timeit(1000))