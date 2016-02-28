class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if len(strs)<2:
            return []
        ret=[]
        data={}
        for i, s in enumerate(strs):
            ss=''.join(sorted(s))
            try:
                if data[ss]>=0:
                    ret.append(strs[data[ss]])
                    ret.append(s)
                    data[ss]=-1
                else:
                    ret.append(s)
            except Exception:
                data[ss]=i
        return ret

def test(*arg):
    for strs in arg:
        print(strs)
        print(Solution().anagrams(strs))
        print()

test(["tea","and","ate","eat","den"])
