class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        elif len(prices) == 2:
            return 0 if prices[0] > prices[1] else prices[1] - prices[0]
        large = 0
        current = 0
        for i in range(len(prices) - 1):
            n = prices[i + 1] - prices[i]
            current += n
            if current > large:
                large = current
            elif current < 0:
                current = 0
        return large


def test(*arg):
    for p in arg:
        print(p, Solution().maxProfit(p))

test([1, 2, 3, 2, 5])
