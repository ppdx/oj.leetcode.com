class Solution:
    # @param path, a string
    # @return a string

    def simplifyPath(self, path):
        _path = [s for s in path.split("/") if s != '' and s != '.']
        i = 0
        while 0<=i < len(_path):
            if(_path[i] == '..'):
                if i==0:
                    _path[0:i + 1] = []
                else:
                    _path[i - 1:i + 1] = []
                    i-=1
            else:
                i += 1
        return '/' + '/'.join(_path)


def test(path):
    print(path, ' => ', Solution().simplifyPath(path))

test("/home/")
test("/a/./b/../../c/")
test("/home/../../..")
test("/..")
