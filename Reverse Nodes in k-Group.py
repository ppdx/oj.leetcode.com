from LinkList import *

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        nextnode = self.countcut(head, k)
        if nextnode is False:
            return head
        result = self.reverse(head)
        tail = head
        head = nextnode
        nextnode = self.countcut(head, k)
        while nextnode is not False:
            tail.next = self.reverse(head)
            tail = head
            head = nextnode
            nextnode = self.countcut(head, k)
        tail.next = head
        return result

    def countcut(self, head, k):
        while k > 1:
            try:
                head = head.__next__
            except Exception:
                return False
            k -= 1
        try:
            p = head.__next__
        except Exception:
            return False
        head.next = None
        return p

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

ll = LinkList([1])
print(ll)
ll.head = Solution().reverseKGroup(ll.head, 2)
print(ll)