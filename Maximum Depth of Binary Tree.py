class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == '__main__':
    r = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, None, TreeNode(5)))
    sol = Solution()
    print((sol.maxDepth(r)))

