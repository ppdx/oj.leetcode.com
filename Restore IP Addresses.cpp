#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int m_atoi(string s, int start, int end)
{
    int res = 0;
    while (start != end)
    {
        res *= 10;
        res += s[start] - '0';
        start++;
    }
    return res;
}

bool isValid(string s, int start, int end)
{
    const int min = 0;
    const int max = 255;
    if (s[start] == '0' && end - start != 1)
        return false;
    int n = m_atoi(s, start, end);
    return n <= max && n >= min;
}

inline int max(int a, int b)
{
    return a <= b ? b : a;
}

inline int min(int a, int b)
{
    return a >= b ? b : a;
}

vector<string> restoreIpAddresses(string s)
{
    vector<string> res;

    int len = s.length();
    int i, j, k;
    i = j = k = 0;
    int topj = min(6, len - 2);
    for (j = max(2, len - 6); j <= topj; j++)
    {
        int topi = min(3, j - 1);
        for (i = max(1, j - 3); i <= topi; i++)
        {
            if (isValid(s, 0, i) && isValid(s, i, j))
            {
                int topk = min(j + 3, len - 1);
                for (k = j + 1; k <= topk; k++)
                {
                    if (isValid(s, j, k) && isValid(s, k, len))
                    {
                        string s1 = s;
                        s1.insert(k, ".");
                        s1.insert(j, ".");
                        s1.insert(i, ".");
                        res.push_back(s1);
                    }
                }
            }
        }
    }
    return res;
}

template<class T>
ostream& operator<<(ostream& os, vector<T> v)
{
    for (auto& e : v)
        os << e << endl;
    return os;
}
int main()
{
    vector<string> tests{ "010010", "25525511135" };
    for (string& s : tests)
    {
        cout << s << ":" << endl;
        cout << restoreIpAddresses(s) << endl;
    }
       
    system("pause");
    return 0;
}