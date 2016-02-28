from LinkList import *

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        newHead = ListNode(head.val + 1)
        pre = head
        isDuplicates = False
        p = head.__next__
        q = newHead
        while p != None:
            if p.val != pre.val:
                if not isDuplicates:
                    q.next = pre
                    q = q.__next__
                    q.next = None
                pre = p
                isDuplicates = False
            else:
                isDuplicates = True
            p = p.__next__
        if not isDuplicates:
            q.next = pre
        return newHead.__next__

ll = LinkList("122")
ll.head = Solution().deleteDuplicates(ll.head)
print(ll)
