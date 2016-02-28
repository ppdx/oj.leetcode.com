class Solution:
    # @param num, a list of integer
    # @return an integer

    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        Max = max(num)
        Min = min(num)
        if Max == Min:
            return 0

        bucketGap = (Max - Min) / len(num) + 1
        bucketLen = (Max - Min) / bucketGap + 1
        bucket = [0xffffffff, -1] * bucketLen

        for n in num:
            ind = (n - Min) / bucketGap
            if n < bucket[ind * 2]:
                bucket[ind * 2] = n
            if n > bucket[ind * 2 + 1]:
                bucket[ind * 2 + 1] = n

        first = bucket[1]
        result = 0
        for i in range(1, bucketLen):
            if bucket[2 * i] == 0xffffffff:
                continue
            tmpmax = bucket[2 * i] - first
            if tmpmax > result:
                result = tmpmax
            first = bucket[i * 2 + 1]
        return result

if __name__ == '__main__':
    nums = [[1], [1, 2, 3, 4, 6, 8],
            [5, 8, 9, 3, 4, 6, 5, 6]]
    sol = Solution()
    for num in nums:
        print(num, end=' ')
        print(sol.maximumGap(num))
