class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        i = int(a, 2)
        j = int(b, 2)
        return bin(i + j)[2:]

a = '1010'
b = '1001'

print((Solution().addBinary(a, b)))
