from LinkList import *

class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def insertionSortList(self, head):
        if head is None or head.__next__ is None:
            return head
        p = head.__next__
        head.next = None
        while p is not None:
            q = p
            p = p.__next__
            if head.val > q.val:
                q.next = head
                head = q
            else:
                r = head
                while r.__next__ is not None and r.next.val < q.val:
                    r = r.__next__
                q.next = r.__next__
                r.next = q
        return head

def test(*lists):
    for l in lists:
        ll = LinkList(l)
        print(ll, '->', end=' ')
        ll.head = Solution().insertionSortList(ll.head)
        print(ll)

cc = [i for i in range(5000, 0, -1)]
test([], [1, 2, 3], [3, 2, 1], [4, 1, 2, 3], cc)
