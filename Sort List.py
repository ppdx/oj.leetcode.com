from LinkList import *

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None:
            return None
        lst = []
        p = head
        while p is not None:
            r = p
            while r.__next__ is not None and r.val < r.next.val:
                r = r.__next__
            lst.append(p)
            p = r.__next__
            r.next = None

        while len(lst) > 1:
            p = lst.pop(0)
            q = lst.pop(0)
            if p.val < q.val:
                r = p
                p = p.__next__
            else:
                r = q
                q = q.__next__
            lst.append(r)
            while p is not None and q is not None:
                if p.val < q.val:
                    r.next = p
                    p = p.__next__
                else:
                    r.next = q
                    q = q.__next__
                r = r.__next__
            if p is not None:
                r.next = p
            else:
                r.next = q
        return lst[0]

def test(*lists):
    for lst in lists:
        ll = LinkList(lst)
        print(ll, '->', end=' ')
        ll.head = Solution().sortList(ll.head)
        print(ll)

test([], [1, 2, 3], [3, 2, 1], [2, 1], [4, 2, 1, 3])
