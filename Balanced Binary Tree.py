# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        b = self.deep(root)
        return b != -1

    def deep(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        l = self.deep(root.left)
        r = self.deep(root.right)
        if l == -1 or r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1

r = TreeNode(1, TreeNode(2))
print((Solution().isBalanced(r)))
