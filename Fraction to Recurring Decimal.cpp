#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <unordered_map>
#include <complex>
using namespace std;

class Solution
{
public:
    string fractionToDecimal(int numerator, int denominator)
    {
        if (denominator == 0)
            return "";
        if (numerator == 0)
            return "0";
        long long n = numerator, d = denominator;
        string res = ((n < 0) ^ (d < 0)) ? "-" : "";
        n = abs(n);
        d = abs(d);
        res += to_string(n / d);
        n %= d;
        if (n == 0)
            return res;
        res.push_back('.');
        unordered_map<long long, size_t> mods;
        auto i = mods.begin();
        while (n)
        {
            if ((i = mods.find(n)) != mods.end())
            {
                res.insert(i->second, "(");
                res.push_back(')');
                return res;
            }
            mods[n] = res.size();
            n *= 10;
            res += to_string(n / d);
            n %= d;
        }
        return res;
    }
};

int main()
{
    auto sol = Solution();
    cout << sol.fractionToDecimal(1, 6) << endl;
    getchar();
    return 0;
}