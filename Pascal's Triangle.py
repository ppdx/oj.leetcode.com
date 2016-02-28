class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        lst = [[1]]
        while numRows > 1:
            lst.append(self.getNext(lst[-1]))
            numRows -= 1
        return lst

    def getNext(self, pre):
        next = [1]
        for i in range(1, len(pre)):
            next.append(pre[i - 1] + pre[i])
        next.append(1)
        return next

print(Solution().generate(5))

