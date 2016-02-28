class Solution:
    # @return an integer

    def atoi(self, str):
        if len(str) < 1:
            return 0
        i = 0
        while i < len(str) and str[i].isspace():
            i += 1
        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1
            sign = 1
        else:
            sign = 1
        j = i
        while j < len(str) and str[j].isdigit():
            j += 1
        ret = int(str[i:j]) if i != j else 0
        ret *= sign
        if ret > 2147483647:
            ret = 2147483647
        elif ret < -2147483648:
            ret = -2147483648
        return ret

if __name__ == '__main__':
    print((Solution().atoi("1")))
