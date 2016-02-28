class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        result = []
        plus = False
        digits[-1] += 1
        for a in digits[::-1]:
            if plus:
                if a + 1 > 9:
                    result.append(a + 1 - 10)
                else:
                    result.append(a + 1)
                    plus = False
            else:
                if a > 9:
                    result.append(a - 10)
                    plus = True
                else:
                    result.append(a)
        if plus:
            result.append(1)
        return result[::-1]

if __name__ == '__main__':
    digits = [9, 9, 9]
    print(Solution().plusOne(digits))