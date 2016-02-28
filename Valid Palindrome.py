class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        ss = ''.join([c for c in s if c.isalnum()]).lower()
        return ss == ss[::-1]

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
sol = Solution()
print("s1 : ", sol.isPalindrome(s1))
print("s2 : ", sol.isPalindrome(s2))
