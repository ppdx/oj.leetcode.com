from queue import Queue

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return "val = " + (self.val.__repr__())

class Tree(object):
    def __init__(self, root):
        self.root = root

    @staticmethod
    def buildTree(s):
        if s == None or len(s) == 0:
            return Tree(None)
        nodeQueue = Queue()
        root = TreeNode(int(s[0]))
        nodeQueue.put(root)
        i = 1
        while i < len(s):
            temp = nodeQueue.get()
            if s[i] != '#':
                temp.left = TreeNode(int(s[i]))
                nodeQueue.put(temp.left)
            i += 1
            if s[i] != '#':
                temp.right = TreeNode(int(s[i]))
                nodeQueue.put(temp.right)
            i += 1
        return Tree(root)

    def postorderTraversal(self):
        data = []

        def view(root):
            if root == None:
                return
            view(root.left)
            view(root.right)
            data.append(root.val)

        view(self.root)
        return data

    def preorderTraversal(self):
        data = []

        def view(root):
            if root == None:
                return
            data.append(root.val)
            view(root.left)
            view(root.right)

        view(self.root)
        return data

    def __repr__(self):
        s = []

        def view(root):
            if root == None:
                s.append("#")
                return
            s.append(root.val.__repr__())
            view(root.left)
            view(root.right)

        view(self.root)
        return " ".join(s)

if __name__ == '__main__':
    str = "123###4"
    r = Tree.buildTree(str)
    print((r.preorderTraversal()))
    print((r.postorderTraversal()))
    print(r)
