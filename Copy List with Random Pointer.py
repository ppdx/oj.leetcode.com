# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        res = RandomListNode(head.label)
        res.next = head.__next__
        res.random = head.random
        table = {head: res}
        p = res
        while p.__next__ is not None:
            q = RandomListNode(p.next.label)
            q.next = p.next.__next__
            q.random = p.next.random
            table[p.next] = q
            p.next = q
            p = q
        p = res
        while p is not None:
            if p.random is not None:
                p.random = table[p.random]
            p = p.__next__
        return res

