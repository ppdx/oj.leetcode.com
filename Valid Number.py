import re


class Solution:
    # @param s, a string
    # @return a boolean

    def isNumber(self, s):
        s = s.strip()
        if re.match(r"^[-+]?(\d+\.?|\.\d+)\d*(e[-+]?\d+)?$", s) is None:
            return False
        else:
            return True


def test(*arg):
    for s in arg:
        print(s, Solution().isNumber(s))

test("0", " 0.1 ", "abc", "1 a", "2e10")
