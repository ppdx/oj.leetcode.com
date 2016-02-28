class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        self.level = []
        self.view(root, 1)
        self.level.reverse()
        return self.level

    def view(self, root, level):
        if root == None:
            return
        if len(self.level) < level:
            self.level.append([])
        self.level[level - 1].append(root.val)
        self.view(root.left, level + 1)
        self.view(root.right, level + 1)

if __name__ == '__main__':
    r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    sol = Solution()
    print((sol.levelOrderBottom(r)))
