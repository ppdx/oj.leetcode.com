class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i = 0
        for e in A:
            if e != elem:
                A[i] = e
                i += 1
        return i

lst = [1, 2, 3, 468, 134, 615, 3, 1]
elem = 3
print((Solution().removeElement(lst, elem)))
print(lst)
