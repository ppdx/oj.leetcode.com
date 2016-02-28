class Solution {
    istringstream iss;
    char operate;
    char read_operate()
    {
        char c;
        do
        {
            iss >> c;
        } while (c == ' ');
        return (operate = c);
    }
    int read_int()
    {
        int n;
        iss >> n;
        return n;
    }
    int expr()
    {
        int left = trim();
        while (true)
            switch (operate)
            {
            case '-':
                left -= trim();
                break;
            case '+':
                left += trim();
                break;
            default:
                return left;
            }
    }
    int trim()
    {
        int left = read_int();
        while (true)
            switch (read_operate())
            {
            case '*':
                left *= read_int();
                break;
            case '/':
                left /= read_int();
                break;
            default:
                return left;
            }
    }
public:
    int calculate(string s) {
        s += 'E';
        iss.str(s);
        return expr();
    }
};
