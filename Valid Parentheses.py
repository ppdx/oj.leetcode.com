class Solution:
    # @return a boolean
    def isValid(self, s):
        lst = []
        try:
            for c in s:
                if c == '{' or c == '(' or c == '[':
                    lst.append(c)
                if c == ')' and lst.pop() != '(':
                    return False
                if c == '}' and lst.pop() != '{':
                    return False
                if c == ']' and lst.pop() != '[':
                    return False
        except Exception:
            return False
        return len(lst) == 0

str = '''double expr(bool get) {
    double left = term(get);
    while (true) {
        switch (curr_tok) {
            case PLUS:
                left += term(true);
                break;
            case MINUS:
                left -= term(true);
                break;
            default:
                return left;
        }
    }
}'''
print((Solution().isValid(str)))
