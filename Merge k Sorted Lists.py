from LinkList import *

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        while len(lists)>1:
            lists.insert(0,self.mergeTwoLists(lists.pop(),lists.pop()))
        return lists[-1]

    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.__next__
        else:
            head = l2
            l2 = l2.__next__
        p = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.__next__
            else:
                p.next = l2
                l2 = l2.__next__
            p = p.__next__
        if l1 is not None:
            p.next = l1
        else:
            p.next = l2
        return head