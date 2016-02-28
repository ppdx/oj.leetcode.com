class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p = ListNode(111111)
        p.next = head
        self.remove(p, n)
        return p.next

    def remove(self, head, n):
        if head == None:
            return 0
        length = self.remove(head.next, n)
        if length == n:
            head.next = head.next.next
        return length + 1

def printList(head):
    if head == None:
        return
    print(head.val, end=' ')
    printList(head.next)

if __name__ == '__main__':
    l = ListNode(1)
    sol = Solution()
    printList(sol.removeNthFromEnd(l, 1))
