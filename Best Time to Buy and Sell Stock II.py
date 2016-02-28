class Solution:
    # @param prices, a list of integer
    # @return an integer

    def maxProfit(self, prices):
        large = 0
        for i in range(len(prices) - 1):
            n = prices[i + 1] - prices[i]
            if n > 0:
                large += n
        return large

def test(*arg):
    for p in arg:
        print(p, Solution().maxProfit(p))

test([1, 2, 3, 2, 5])
