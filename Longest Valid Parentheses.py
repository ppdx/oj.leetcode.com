class Solution:
    # @param s, a string
    # @return an integer

    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0
        stack = []
        maxLen = 0
        lastError = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                    maxLen = max(
                        maxLen, i - lastError if len(stack) == 0 else i - stack[-1])
                else:
                    lastError = i
        return maxLen

if __name__ == '__main__':
    s = ")()()("
    print(s)
    print(Solution().longestValidParentheses(s))
