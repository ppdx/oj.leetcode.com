from LinkList import *

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head is None or head.__next__ is None:
            return head
        res=p=ListNode(0)
        tail=q=ListNode(0)
        while head is not None:
            if head.val<x:
                p.next=head
                p=p.__next__
            else:
                q.next=head
                q=q.__next__
            head=head.__next__
        q.next=None
        p.next=tail.__next__
        return res.__next__

def test(*arg):
    for l,n in arg:
        ll=LinkList(l)
        print(ll,n)
        ll.head=Solution().partition(ll.head,n)
        print("==>",ll)

test(([1,4,3,2,5,2],3))

