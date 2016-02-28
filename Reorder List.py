from LinkList import *

class Solution:
    # @param head, a ListNode
    # @return nothing

    def reorderList(self, head):
        length = self.getlength(head)
        if length <= 2:
            return head
        tail = self.cut(head, length / 2)
        tail = self.reverse(tail)

        ret = head
        p = ret
        head = head.__next__
        while head is not None and tail is not None:
            ret.next = tail
            tail = tail.__next__
            ret = ret.__next__

            ret.next = head
            head = head.__next__
            ret = ret.__next__
        ret.next = tail
        return p

    def getlength(self, head):
        length = 0
        while head is not None:
            length += 1
            head=head.__next__
        return length

    def cut(self, head, length):
        while length > 1:
            head = head.__next__
            length -= 1
        tmp = head.__next__
        head.next = None
        return tmp

    def reverse(self, head):
        if head is None:
            return head
        h = head
        p = h.__next__
        h.next = None
        while p is not None:
            q = p
            p = p.__next__
            q.next = h
            h = q
        return h

lst = list(range(100))
ll = LinkList(lst)
ll.head = Solution().reorderList(ll.head)
print(ll)