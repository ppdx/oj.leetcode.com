class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left == None and root.right == None and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

r = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
             TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print((Solution().hasPathSum(r, 22)))
