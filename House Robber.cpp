#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <limits>
#include <random>
#include <functional>
#include <unordered_set>
#include <numeric>
#include <cassert>
#include <array>
using namespace std;

int rob(vector<int> &num)
{
    int len = num.size();
    if (len == 0) return 0;
    vector<int> dp(num);
    dp[1] = max(dp[0], dp[1]);
    for (int i = 2; i < len; i++)
        dp[i] = max(dp[i - 2] + dp[i], dp[i - 1]);
    return dp.back();
}

int main()
{
    vector<int> data{ 1,2,3 };
    cout << rob(data) << endl;
}