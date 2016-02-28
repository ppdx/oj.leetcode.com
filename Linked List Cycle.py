from LinkList import *

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        slow=fast=head
        try:
            slow=slow.__next__
            fast=fast.next.__next__
            while slow != fast:
                slow=slow.__next__
                fast=fast.next.__next__
            return True
        except Exception:
            return False
