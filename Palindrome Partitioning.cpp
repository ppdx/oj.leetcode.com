#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <unordered_map>
#include <complex>
#include <cassert>
using namespace std;

class Solution
{
public:
    vector<vector<string>> partition(string s)
    {
        vector<vector<string>> res;
        if (s.size() == 0)
            return res;
        for (int i = 1; i <= s.size(); ++i)
        {
            if (isPalindrome(s, 0, i))
            {
                auto tail = partition(s.substr(i));
                if (tail.size() == 0) tail.push_back(vector<string>{});
                for (auto& ss : tail)
                {
                    res.push_back(vector<string>{});
                    auto& current = res.back();
                    current.push_back(s.substr(0, i));
                    current.insert(current.end(), ss.begin(), ss.end());
                }
            }
        }
        return res;
    }

    bool isPalindrome(string s, int start, int end)
    {
        assert(start <= end);
        if (start == end--)
            return true;
        while (start < end)
            if (s[start++] != s[end--])
                return false;
        return true;
    }
};

void printResult(vector<vector<string>> vvs)
{
    for (auto& vs : vvs)
    {
        for (auto& s : vs)
        {
            cout << "\"" << s << "\", ";
        }
        cout << endl;
    }
}

int main()
{
    printResult(Solution{}.partition("aab"));
    getchar();
}