class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return super(ListNode, self).__repr__() + " val = %d" % self.val

class LinkList(object):
    def __init__(self, lst=[]):
        if len(lst) == 0:
            self.head = None
        else:
            self.head = ListNode(int(lst[0]))
        pre = self.head
        for i in lst[1:]:
            pre.next = ListNode(int(i))
            pre = pre.__next__

    def __repr__(self):
        pre = self.head
        lst = []
        while pre != None:
            lst.append(pre.val)
            pre = pre.__next__
        return str(lst)

    def reverse(self):
        if self.head == None:
            return self.head
        h = self.head
        p = h.__next__
        h.next = None
        while p != None:
            q = p
            p = p.__next__
            q.next = h
            h = q
        self.head = h

    def getNode(self, n):
        h = self.head
        while n > 0:
            h = h.__next__
            n -= 1
        return h

    def __len__(self):
        l = 0
        h = self.head
        while h != None:
            h = h.__next__
            l += 1
        return l

if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    ll = LinkList(lst)
    ll.reverse()
    print(ll)
    print(len(ll))
    print(ll.getNode(2).val)
