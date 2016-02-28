class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean

    def isMatch(self, s, p):
        i = j = 0
        backup_i = backup_j = -1
        while i < len(s):
            if s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            elif p[j] == '*':
                backup_j = j
                backup_i = i
                j += 1
            else:
                if backup_j == -1:
                    return False
                j = backup_j
                i = backup_i + 1
                backup_i = i
                j += 1
        while j < len(p):
            if p[j] != '*':
                return False
            j += 1
        return True


def test(*args):
    for arg in args:
        print(arg, Solution().isMatch(*arg))

test(("aa", "a"), ("aa", "aa"), ("aaa", "aa"), ("aa", "*"),
     ("aa", "a*"), ("ab", "?*"), ("aab", "c*a*b"))
