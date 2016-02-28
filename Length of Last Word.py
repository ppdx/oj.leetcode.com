class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == "":
            return 0
        l = s.split()
        return 0 if len(l) == 0 else len(s.split()[-1])

print(Solution().lengthOfLastWord(" "))
