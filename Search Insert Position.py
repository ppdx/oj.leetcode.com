class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer

    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0
        return self.search(A, target, 0, len(A))

    def search(self, A, target, left, right):
        if left == len(A):
            return left
        if left >= right:
            if A[left] >= target:
                return left
            else:
                return left + 1
        mid = (left + right) // 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return self.search(A, target, left, mid - 1)
        else:
            return self.search(A, target, mid + 1, right)


def test(A, target):
    print((A, target), " ==> ", Solution().searchInsert(A, target))


def tests(X):
    for x in X:
        test(*x)

tests([[[1, 3], 2],
       [[1, 3, 5, 6], 5],
       [[1, 3, 5, 6], 2],
       [[1, 3, 5, 6], 7],
       [[1, 3, 5, 6], 0]])
