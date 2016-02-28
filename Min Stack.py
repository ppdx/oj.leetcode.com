class MinStack:
    def __init__(self):
        self.lst = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.lst.append(x)

    # @return nothing
    def pop(self):
        self.lst.pop()

    # @return an integer
    def top(self):
        self.lst[-1]

    # @return an integer
    def getMin(self):
        return min(self.lst)
