from LinkList import *


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n or head is None:
            return head

        p = ListNode(333)
        p.next = head
        head = p
        length = m
        while length > 1:
            head = head.__next__
            length -= 1
        mid = head.__next__
        head.next = None

        tail = self.cut(mid, n - m + 1)
        q = self.reverse(mid)
        head.next = q
        mid.next = tail
        return p.__next__

    def cut(self, head, length):
        while length > 1:
            head = head.__next__
            length -= 1
        tmp = head.__next__
        head.next = None
        return tmp

    def reverse(self, head):
        if head == None:
            return head
        h = head
        p = h.__next__
        h.next = None
        while p != None:
            q = p
            p = p.__next__
            q.next = h
            h = q
        return h


if __name__ == '__main__':
    l = "35"
    sol = Solution()
    ll = LinkList(l)
    print(ll)
    ll.head = sol.reverseBetween(ll.head, 1, 2)
    print(ll)
