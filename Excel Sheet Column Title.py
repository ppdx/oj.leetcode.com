class Solution:
    # @return a string
    def convertToTitle(self, num):
        table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = []
        while num != 0:
            num -= 1
            r.append(table[(num) % 26])
            num /= 26
        return "".join(r[::-1])

print(Solution().convertToTitle(52))
