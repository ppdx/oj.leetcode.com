class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        lst = [1]
        while rowIndex > 0:
            lst = self.getNext(lst)
            rowIndex -= 1
        return lst

    def getNext(self, pre):
        next = [1]
        for i in range(1, len(pre)):
            next.append(pre[i - 1] + pre[i])
        next.append(1)
        return next

print(Solution().getRow(5))
