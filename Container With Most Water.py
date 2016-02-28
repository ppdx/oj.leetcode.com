class Solution:
    # @return an integer
    def maxArea(self, height):
        large = 0
        i = 0
        j = len(height) - 1
        while i < j:
            large = max(large, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                tmp = height[i]
                i += 1
                while i < j and height[i] < tmp:
                    i += 1
            else:
                tmp = height[j]
                j -= 1
                while i < j and height[j] < tmp:
                    j -= 1
        return large

sol=Solution()
print(sol.maxArea([1,2,3]))