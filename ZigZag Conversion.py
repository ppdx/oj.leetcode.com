# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
# like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows <= 1:
            return s
        result = [[] for i in range(nRows)]
        row = 0
        step = 1
        for c in s:
            if row == nRows - 1:
                step = -1
            elif row == 0:
                step = 1
            result[row].append(c)
            row += step
        return "".join([''.join(s) for s in result])

if __name__ == '__main__':
    str = "ABCD"
    nRows = 2
    result = Solution().convert(str, nRows)
    # truth="PAHNAPLSIIGYIR"
    print(result)
    # print result==truth
