# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(5), TreeNode(3)))
print((Solution().isSymmetric(root)))
