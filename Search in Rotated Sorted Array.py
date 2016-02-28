class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer

    def search(self, A, target):
        if len(A) < 5:
            try:
                return A.index(target)
            except Exception:
                return -1

        low = 0
        high = len(A) - 1
        while low <= high:
            if A[low] < A[high]:
                return self.binarysearch(A, low, high, target)
            mid = (low + high) / 2
            if A[mid] == target:
                return mid
            if A[mid] >= A[low]:
                if A[mid] >= target >= A[low]:
                    return self.binarysearch(A, low, mid - 1, target)
                else:
                    low = mid + 1
                    continue
            else:
                if A[mid] <= target <= A[high]:
                    return self.binarysearch(A, mid + 1, high, target)
                else:
                    high = mid - 1
                    continue
        return -1

    def binarysearch(self, a, low, high, target):
        while low <= high:
            if target < a[low] or target > a[high]:
                return -1
            mid = low + (high - low) / 2
            if a[mid] == target:
                return mid
            elif a[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


def test(*pairs):
    sol = Solution()
    for l, t in pairs:
        print(l, t, sol.search(l, t))

test(([4, 5, 6, 7, 0, 1, 2], 4),([5,1,2,3,4], 1))
