class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        rows = len(word1) + 1
        cols = len(word2) + 1
        data = [list(range(cols)) for i in range(rows)]

        for i in range(rows):
            data[i][0] = i
        for j in range(cols):
            data[0][j] = j

        for i in range(1, rows):
            c1 = word1[i - 1]
            for j in range(1, cols):
                c2 = word2[j - 1]
                if c1 == c2:
                    data[i][j] = data[i - 1][j - 1]
                else:
                    data[i][j] = min(data[i - 1][j - 1], data[i][j - 1], data[i - 1][j]) + 1
        return data[rows - 1][cols - 1]

def test(*args):
    for arg in args:
        print(arg)
        print(Solution().minDistance(*arg))

test(('123', '234'))
