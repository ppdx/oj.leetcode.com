class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        ver1 = [int(s) for s in version1.split('.')]
        ver2 = [int(s) for s in version2.split('.')]
        if len(ver1) > len(ver2):
            ver2 = ver2 + [0] * (len(ver1) - len(ver2))
        else:
            ver1 = ver1 + [0] * (len(ver2) - len(ver1))
        return cmp(ver1, ver2)

if __name__ == '__main__':
    version1 = '1.0'
    version2 = '1'
    print(Solution().compareVersion(version1, version2))