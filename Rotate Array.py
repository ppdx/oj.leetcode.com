class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.

    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k - 1::-1] + nums[-1:-k - 1:-1]
        nums[:] = nums[::-1]

if __name__ == '__main__':
    sol = Solution()
    args = [([1, 2, 3, 4, 5, 6, 7], 3),
            ([1, 2], 3),
            ([1], 0)]
    for one in args:
        print(one, "=>")
        sol.rotate(*one)
        print(one)
