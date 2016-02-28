import collections
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dic=collections.defaultdict(list)
        for i,n in enumerate(nums):
            dic[n].append(i)
        for l in list(dic.values()):
            if len(l)<2:
                continue
            l.sort()
            if min(l[i]-l[i-1] for i in range(1,len(l)))<=k:
                return True
        return False

test=[1,2,3,4,5,2]
print((Solution().containsNearbyDuplicate([-1,-1], 1)))
