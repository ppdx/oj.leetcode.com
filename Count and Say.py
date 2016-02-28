class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"
        source = self.countAndSay(n - 1)
        result = []
        pre = source[0]
        count = 1
        for c in source[1:]:
            if c == pre:
                count += 1
            else:
                result.append(str(count))
                result.append(str(pre))
                pre = c
                count = 1
        result.append(str(count))
        result.append(str(pre))
        return "".join(result)

print(Solution().countAndSay(5))
