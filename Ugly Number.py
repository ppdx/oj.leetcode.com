class Solution(object):
    factors = [2, 3, 5]

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for fact in self.factors:
            while num % fact == 0:
                num /= fact
        return num == 1

if __name__ == '__main__':
    s = Solution()
    for n in [1, 2, 6, 8, 14]:
        print((n, s.isUgly(n)))
