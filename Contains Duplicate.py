class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        s=set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

test=[1,2,3,4,5,2]
print((Solution().containsDuplicate(test)))
