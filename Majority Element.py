class Solution:
    # @param num, a list of integers
    # @return an integer

    def majorityElement(self, num):
        table = { }
        for n in num:
            try:
                table[n] += 1
            except Exception:
                table[n] = 1

        i_max = 0
        n_max = 0
        for (i, n) in list(table.items()):
            if n > n_max:
                i_max = i
                n_max = n
        return i_max

print(Solution().majorityElement([1, 2, 3, 4, 1, 5, 1, 2, 1, 1, 1, 1]))
