import math

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == '+':
                x = stack.pop()
                y = stack.pop()
                stack.append(y + x)
                # print("%d %s %d = %d" % (y,i,x,stack[-1]))
            elif i == '-':
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
                # print("%d %s %d = %d" % (y,i,x,stack[-1]))
            elif i == '*':
                x = stack.pop()
                y = stack.pop()
                stack.append(y * x)
                # print("%d %s %d = %d" % (y,i,x,stack[-1]))
            elif i == '/':
                x = stack.pop()
                y = stack.pop()
                r = y / x
                if r >= 0:
                    stack.append(int(math.floor(r)))
                else:
                    stack.append(int(math.ceil(r)))
                    # print("%d %s %d = %d" % (y,i,x,stack[-1]))
            else:
                stack.append(int(i))
        return stack.pop()

lst = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print((Solution().evalRPN(lst)))
