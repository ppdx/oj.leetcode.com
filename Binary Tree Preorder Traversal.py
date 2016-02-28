class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        self.data = []
        self.view(root)
        return self.data

    def view(self, root):
        if root == None:
            return
        self.data.append(root.val)
        self.view(root.left)
        self.view(root.right)
