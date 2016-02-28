class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return []
        ret = []
        stack = [('', n, 0)]
        while len(stack) > 0:
            s, n, l = stack.pop()
            if n == 0 and l == 0:
                ret.append(s)
                continue
            if n>0:
                stack.append((s + '(', n - 1, l + 1))
            if l>0:
                stack.append((s + ')', n, l - 1))
        return ret

print(Solution().generateParenthesis(4))