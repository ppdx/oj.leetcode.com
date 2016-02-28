class Solution(object):
    dozens = ['twenty', 'thirty', 'forty', 'fifty',
              'sixty', 'seventy', 'eighty', 'ninety']
    tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    unit = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    scale = ['thousand', 'million', 'billion']

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:return unit[0]


    def splitWithscale(self,num):
        res=[]


if __name__ == '__main__':
    print((Solution().nthUglyNumber(10)))
