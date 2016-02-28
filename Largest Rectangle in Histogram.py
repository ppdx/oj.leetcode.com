class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if len(height) == 0:
            return 0
        large = 0
        stack = []
        for i, h in enumerate(height):
            while len(stack) > 0 and h <= height[stack[-1]]:
                x = stack.pop()
                if len(stack) == 0:
                    large = max(large, i * height[x])
                else:
                    large = max(large, (i - stack[-1] - 1) * height[x])
            stack.append(i)

        while len(stack) > 0:
            x = stack.pop()
            if len(stack) == 0:
                large = max(large, len(height) * height[x])
            else:
                large = max(large, (len(height) - stack[-1] - 1) * height[x])
        return large

def test(*args):
    for arg in args:
        print(arg, Solution().largestRectangleArea(arg))

test([2, 1, 5, 6, 2, 3])
