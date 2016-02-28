class Solution:
    # @return an integer
    def romanToInt(self, s):
        num = 0
        i = 0
        while len(s) > i:
            if s[i] == 'M':  # +1000
                num += 1000
            elif s[i] == 'D':  # +500
                num += 500
            elif s[i] == 'C':  # +100
                if len(s) > i + 1 and s[i + 1] == 'M':
                    num += 900
                    i += 1
                elif len(s) > i + 1 and s[i + 1] == 'D':
                    num += 400
                    i += 1
                else:
                    num += 100
            elif s[i] == 'L':  # +50
                num += 50
            elif s[i] == 'X':  # +10
                if len(s) > i + 1 and s[i + 1] == 'C':
                    num += 90
                    i += 1
                elif len(s) > i + 1 and s[i + 1] == 'L':
                    num += 40
                    i += 1
                else:
                    num += 10
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'I':
                if len(s) > i + 1 and s[i + 1] == 'X':
                    num += 9
                    i += 1
                elif len(s) > i + 1 and s[i + 1] == 'V':
                    num += 4
                    i += 1
                else:
                    num += 1
            i += 1
        return num


