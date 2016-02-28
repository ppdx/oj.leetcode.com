from LinkList import *

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow=fast=head
        try:
            slow=slow.__next__
            fast=fast.next.__next__
            while slow != fast:
                slow=slow.__next__
                fast=fast.next.__next__
            fast=head
            while slow != fast:
                slow=slow.__next__
                fast=fast.__next__
            return slow
        except Exception:
            return None
