class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean

    def searchMatrix(self, matrix, target):
        line = self.choseline(matrix, target)
        if line == len(matrix):
            return False
        else:
            return self.binarySearch(matrix[line], target)

    @staticmethod
    def choseline(matrix, target):
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) / 2
            if mid - left == 1 and matrix[left][0] <= target < matrix[mid][0]:
                return left
            elif right - mid == 1 and matrix[mid][0] <= target < matrix[right][0]:
                return mid
            if matrix[mid][0] == target:
                return mid
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return min(left, right)

    @staticmethod
    def binarySearch(line, target):
        left = 0
        right = len(line) - 1
        while left <= right:
            mid = (left + right) / 2
            if line[mid] == target:
                return True
            elif line[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

def test(*args):
    for arg in args:
        print(arg)
        print(Solution().searchMatrix(*arg))

test(([[1], [3]], 3),
     ([[1, 3]], 3),
     ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
