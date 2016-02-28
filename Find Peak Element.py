class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 1:
            return 0
        if num[0] > num[1]:
            return 0
        if num[-1] > num[-2]:
            return len(num) - 1
        return self.find(num, 1, len(num) - 2)

    def find(self, num, left, right):
        if left == right:
            return left
        mid = (left + right) // 2
        if num[mid - 1] > num[mid]:
            return self.find(num, left, mid - 1)
        elif num[mid] > num[mid + 1]:
            return mid
        else:
            return self.find(num, mid + 1, right)

lst = [1, 2, 3, 1]
sol = Solution()
print((sol.findPeakElement(lst)))

