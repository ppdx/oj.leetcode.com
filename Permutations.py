class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers

    def permute(self, num):
        num.sort()
        ret = [[i for i in num]]
        next = num
        while True:
            next = self.nextPermutation(next)
            if next != ret[0]:
                ret.append([i for i in next])
            else:
                break
        return ret

    def nextPermutation(self, num):
        if len(num) < 2:
            return num

        i = len(num) - 1
        while i > 0 and num[i - 1] >= num[i]:
            i -= 1

        if i == 0:
            return num[::-1]

        j = len(num) - 1
        while j >= i and num[j] <= num[i - 1]:
            j -= 1

        num[j], num[i - 1] = num[i - 1], num[j]
        return num[:i] + num[i:][::-1]


def test(*arg):
    for l in arg:
        print(l, Solution().permute(l))

test([1, 2, 3], [3, 2, 1], [1, 5, 1],[1,1,2])
