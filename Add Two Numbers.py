from LinkList import *

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        p=head=ListNode(l1.val+l2.val)
        l1=l1.__next__
        l2=l2.__next__
        if p.val>9:
            p.val-=10
            up=1
        else:
            up=0
        while l1 is not None and l2 is not None:
            p.next=ListNode(l1.val+l2.val+up)
            p=p.__next__
            l1=l1.__next__
            l2=l2.__next__
            if p.val>9:
                p.val-=10
                up=1
            else:
                up=0

        if l1 is None:
            last=l2
        else:
            last=l1
        while last is not None:
            p.next=ListNode(last.val+up)
            p=p.__next__
            last=last.__next__
            if p.val>9:
                p.val-=10
                up=1
            else:
                up=0
        if up==1:
            p.next=ListNode(1)
        return head

def test(*nums):
    for num in nums:
        l1=LinkList(num[0])
        l2=LinkList(num[1])
        l3=LinkList()
        l3.head=Solution().addTwoNumbers(l1.head,l2.head)
        print(l1,"+",l2,'=',l3)

test([[2,4,3],[5,6,4]])
