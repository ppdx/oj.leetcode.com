class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        ret = set()

        positive = { }
        negative = { }
        zero = 0
        for n in num:
            if n > 0:
                try:
                    positive[n] += 1
                except Exception:
                    positive[n] = 1
            elif n < 0:
                try:
                    negative[n] += 1
                except Exception:
                    negative[n] = 1
            else:
                zero += 1
        if zero >= 3:
            ret.add((0, 0, 0))
        if zero > 0:
            for n in positive:
                if -n in negative:
                    ret.add((-n, 0, n))
        for n in negative:
            for m in positive:
                x = -m - n
                if x in negative:
                    if n == x and negative[n] > 1:
                        ret.add((n, n, m))
                    elif n > x:
                        ret.add((x, n, m))
                    elif n < x:
                        ret.add((n, x, m))
                elif x in positive:
                    if m == x and positive[m] > 1:
                        ret.add((n, m, m))
                    elif m > x:
                        ret.add((n, x, m))
                    elif m < x:
                        ret.add((n, m, x))
        return [list(i) for i in ret]

def test(*nums):
    sol = Solution()
    for num in nums:
        print(num, '->', sol.threeSum(num))

test([-1, 0, 1, 2, -1, -4, 3])
