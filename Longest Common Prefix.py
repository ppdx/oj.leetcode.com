class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        minLen = len(min(strs, key=len))
        for i in range(minLen, 0, -1):
            subStr = strs[0][0:i]
            try:
                for str in strs:
                    if not str.startswith(subStr):
                        raise Exception()
                return subStr
            except Exception:
                continue
        return 0

if __name__ == '__main__':
    strs = "where when who whom".split()
    sol = Solution()
    print((sol.longestCommonPrefix(strs)))
