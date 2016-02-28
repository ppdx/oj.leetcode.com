class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        p = head
        q = head.next
        while q != None:
            if p.val != q.val:
                p.next = q
                p = q
            q = q.next
        p.next = q
        return head

def printList(head):
    if head == None:
        return
    print(head.val, end=' ')
    printList(head.next)

l = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
printList(Solution().deleteDuplicates(l))
