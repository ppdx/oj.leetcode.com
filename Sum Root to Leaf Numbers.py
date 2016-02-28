from TreeNode import *

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val
        return self.sumPath(root.left, root.val) + self.sumPath(root.right, root.val)

    def sumPath(self, root, sum):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return sum * 10 + root.val
        else:
            return self.sumPath(root.left, sum * 10 + root.val) + self.sumPath(root.right, sum * 10 + root.val)

t = Tree.buildTree("12##3##")
print(t)
print(Solution().sumNumbers(t.root))
