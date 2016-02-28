class Solution:
    # @param prices, a list of integer
    # @return an integer

    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        sub = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        if len(prices) == 2:
            return 0 if sub[0] < 0 else sub[0]

        large = self.findMax(sub)
        i = 0
        while i < len(sub):
            if sub[i] < 0:
                current = self.findMax(sub[:i])
                while i < len(sub) and sub[i] <= 0:
                    i += 1
                current += self.findMax(sub[i:])
                if current > large:
                    large = current
            i += 1
        return large

    def findMax(self, sub):
        large = 0
        current = 0
        for n in sub:
            current += n
            if current < 0:
                current = 0
            elif current > large:
                large = current
        return large


def test(*arg):
    for p in arg:
        print(p, Solution().maxProfit(p))

