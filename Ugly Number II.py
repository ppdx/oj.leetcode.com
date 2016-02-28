class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = [1]
        i2 = i3 = i5 = 0
        for _ in range(1, n):
            m2 = uglys[i2]*2
            m3 = uglys[i3]*3
            m5 = uglys[i5]*5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            uglys.append(m)
        return uglys[-1]

if __name__ == '__main__':
    print((Solution().nthUglyNumber(10)))
