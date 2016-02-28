class Solution:
    # @return a float

    def findMedianSortedArrays(self, A, B):
        total = len(A) + len(B)
        if total % 2 == 1:
            return self.findKth(A, B, total / 2 + 1)
        else:
            return (self.findKth(A, B, total / 2) + self.findKth(A, B, total / 2 + 1)) / 2.0

    def findKth(self, a, b, k):
        if len(a) > len(b):
            return self.findKth(b, a, k)
        if len(a) == 0:
            return b[k - 1]
        if k == 1:
            return min(a[0], b[0])
        pa = min(k / 2, len(a))
        pb = k - pa
        if a[pa - 1] < b[pb - 1]:
            return self.findKth(a[pa:], b, k - pa)
        elif a[pa - 1] > b[pb - 1]:
            return self.findKth(a, b[pb:], k - pb)
        else:
            return a[pa - 1]

print(Solution().findMedianSortedArrays([1, 2, 3], [1, 2, 2]))