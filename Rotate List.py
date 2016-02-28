from LinkList import *

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k==0:
            return head
        length=self.length(head)
        if length==1 or length==0:
            return head
        k%=length
        if k==0:
            return head
        tail=self.cut(head,length-k)
        p=tail
        while p.__next__ is not None:
            p=p.__next__
        p.next=head
        return tail

    def length(self, h):
        l = 0
        while h != None:
            h = h.__next__
            l += 1
        return l

    def cut(self,head,l):
        if l==0:
            return head
        while l!=1:
            head=head.__next__
            l-=1
        p=head.__next__
        head.next=None
        return p

ll=LinkList([1,2])
print(ll)
ll.head=Solution().rotateRight(ll.head,3)
print(ll)
