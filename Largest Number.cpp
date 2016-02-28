#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
using namespace std;

class Solution
{
public:
    int size(int n)
    {
        int i = 1;
        while (n >= 10)
        {
            i += 1;
            n /= 10;
        }
        return i;
    }
    string largestNumber(vector<int> &num)
    {
        sort(num.begin(), num.end(), [this](int a, int b) {
            int len1 = size(a);
            int len2 = size(b);
            double c = a * pow(10, len2) + b;
            double d = b * pow(10, len1) + a;
            return c > d ? true : false;
        });
        ostringstream oss;
        for (auto n : num)
            oss << n;
        auto ret = oss.str();
        ret.erase(0, ret.find_first_not_of("0"));
        return ret.empty() ? "0" : ret;
    }
};

int main()
{
    vector<int> data = { 999999998,999999997,999999999 };
    cout << Solution{}.largestNumber(data) << endl;
    for (auto n : data)
        cout << n << endl;
    system("pause");
    return 0;
}