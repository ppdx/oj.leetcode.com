class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) < 2:
            return len(s)
        length_max=0
        current_str=''
        for c in s:
            index=current_str.find(c)
            if index ==-1:
                current_str+=c
            else:
                if len(current_str)>length_max:
                    length_max=len(current_str)
                current_str=current_str[index+1:]+c
        if len(current_str)>length_max:
            length_max=len(current_str)
        return length_max

def test(*strs):
    for str in strs:
        print(str, Solution().lengthOfLongestSubstring(str))

test("abcabcbb", "bbbb","qopubjguxhxdipfzwswybgfylqvjzhar",
     "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco")
