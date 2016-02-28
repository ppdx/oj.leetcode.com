class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        longest = ""
        for i in range(len(s)):
            b = a = i
            while s[b] == s[a]:
                if a != 0 and b != len(s) - 1:
                    a -= 1
                    b += 1
                else:
                    if b - a + 1 > len(longest):
                        longest = s[a:b + 1]
                    break
            else:
                if b - a - 1 > len(longest):
                    longest = s[a + 1:b]

            if i == len(s) - 1:
                break
            a = i
            b = i + 1
            while s[a] == s[b]:
                if a != 0 and b != len(s) - 1:
                    a -= 1
                    b += 1
                else:
                    if b - a + 1 > len(longest):
                        longest = s[a:b + 1]
                    break
            else:
                if b - a - 1 > len(longest):
                    longest = s[a + 1:b]

        return longest

def test(*strs):
    sol = Solution()
    for str in strs:
        print(str, sol.longestPalindrome(str))

test("abcddcba", "", "a", "abcdc")