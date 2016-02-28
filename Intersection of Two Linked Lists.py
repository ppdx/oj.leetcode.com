from LinkList import *

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lengthA = self.length(headA)
        lengthB = self.length(headB)
        sub = lengthA - lengthB
        if sub >= 0:
            while sub > 0:
                headA = headA.__next__
                sub -= 1
        else:
            sub = -sub
            while sub > 0:
                headB = headB.__next__
                sub -= 1
        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.__next__
            headB = headB.__next__
        return None

    def length(self, head):
        l = 1
        while head != None:
            head = head.__next__
            l += 1
        return l

lla = LinkList()
llb = LinkList([2, 3])
lla.head = llb.getNode(1)
print(lla)
print(llb)
print(Solution().getIntersectionNode(lla.head, llb.head))
