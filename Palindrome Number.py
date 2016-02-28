class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        length = self.getlen(x)
        # print length
        for i in range(0, length // 2):
            if self.numAt(x, i) != self.numAt(x, length - 1 - i):
                # print i
                return False
        return True

    def getlen(self, x):
        length = 1
        while x >= 10:
            length += 1
            x = x // 10
        return length

    def numAt(self, x, index):
        while index != 0:
            x = x // 10
            index -= 1
        return x % 10

num = 12321
print(Solution().isPalindrome(num))
