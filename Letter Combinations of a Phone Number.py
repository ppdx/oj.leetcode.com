class Solution:
    maps = { 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz' }
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if digits == '':
            return ['']
        results = []
        nums = [int(s) for s in list(digits)]
        limits = [len(self.maps[i]) for i in nums]
        now = [0] * len(nums)
        while limits[0] > now[0]:
            r = []
            for i, n in enumerate(now):
                r.append(self.maps[nums[i]][n])
            results.append(''.join(r))

            now[-1] += 1
            for i in range(len(now) - 1, 0, -1):
                if now[i] == limits[i]:
                    now[i] = 0
                    now[i - 1] += 1
                else:
                    break
        return results

if __name__ == '__main__':
    digits = '23'
    print(Solution().letterCombinations(digits))