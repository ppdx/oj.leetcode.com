class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        res = []
        length = len(words)
        i = 0
        while i < length:
            rowlen = 0
            j = i
            while j < length and rowlen + len(words[j]) <= L:
                rowlen += len(words[j]) + 1
                j += 1
            if j - i == 1:
                res.append(words[i] + ' ' * (L - len(words[i])))
                i = j
                continue
            charlen = rowlen - (j - i)
            meanspace = (L - charlen) / (j - i - 1) if j < length else 1
            leftspace = (L - charlen) % (j - i - 1) if j < length else L - charlen - (j - i - 1)
            line = []
            for k in range(i, j - 1):
                line.append(words[k])
                line.append(' ' * meanspace)
                if j < length and leftspace > 0:
                    line.append(' ')
                    leftspace -= 1
            line.append(words[j - 1])
            if leftspace > 0:
                line.append(' ' * leftspace)
            res.append(''.join(line))
            i = j
        return res

def test(*arg):
    for w, l in arg:
        print((w, l, Solution().fullJustify(w, l)))

test(([""], 0), (["This", "is", "an", "example", "of", "text", "justification."], 16),
     (["Here", "is", "an", "example", "of", "text", "justification."], 14),
     (
     ["My", "momma", "always", "said,", '"Life', "was", "like", "a", "box", "of", "chocolates.", "You", "never", "know",
      "what", "you're", "gonna", "get."], 20))
