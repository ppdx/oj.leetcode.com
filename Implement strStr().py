class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        try:
            return haystack.index(needle)
        except Exception:
            return -1

haystack = 'adhd'
needle = 'hd'
print((Solution().strStr(haystack, needle)))
