from LinkList import *

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        p = head
        if p is not None and p.__next__ is not None:
            q = p
            p = p.__next__
            q.next = p.__next__
            p.next = q
            head=p
            p=p.__next__
        while p is not None and p.__next__ is not None and p.next.__next__ is not None:
            q = p.__next__
            p.next=p.next.__next__
            p = q.__next__
            q.next = p.__next__
            p.next = q
            p=p.__next__
        return head

ll=LinkList(list(range(12)))
print(ll)
ll.head=Solution().swapPairs(ll.head)
print(ll)