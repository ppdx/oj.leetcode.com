# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return
        root.left.next = root.right
        self.connect2(root.left, root.right)
        self.connect(root.left)
        self.connect(root.right)

    def connect2(self, r1, r2):
        if r1 == None or r2 == None:
            return
        if r1.left == None and r1.right == None:
            return
        r1.right.next = r2.left
        self.connect2(r1, r2)

if __name__ == '__main__':
    Solution().connect(None)