class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]

    def searchRange(self, A, target):
        if len(A) == 0:
            return [-1, -1]
        if len(A) == 1:
            if A[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] == target:
                break
            elif A[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return [-1, -1]

        left = mid
        while left >= 0 and A[left] == target:
            left -= 1

        right = mid
        while right < len(A) and A[right] == target:
            right += 1
        return [left + 1, right - 1]

A = [2,2]
target = 1
print(A)
print(target)
print(Solution().searchRange(A, target))
