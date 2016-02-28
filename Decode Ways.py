class Solution:
    # @param s, a string
    # @return an integer

    def numDecodings(self, s):
        if len(s) == 0 or s.startswith('0'):
            return 0
        elif len(s) == 1:
            return 1

        dp = [0] * len(s)
        dp[0] = 1
        if int(s[:2]) < 27:
            dp[1] += 1
        if s[1] != '0':
            dp[1] += 1

        for i in range(2, len(s)):
            if s[i - 1] == '0':
                if s[i] == '0':
                    return 0
                else:
                    dp[i] = dp[i - 1]
            else:
                if int(s[i - 1:i + 1]) < 27:
                    dp[i] += dp[i - 2]
                if s[i] != '0':
                    dp[i] += dp[i - 1]

        return dp[-1]


def test(*args):
    for arg in args:
        print(arg.__repr__(), Solution().numDecodings(arg))

test("", "12", "10",
     "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
