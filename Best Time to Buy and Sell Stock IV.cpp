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
#include <utility>
using namespace std;

class Solution
{
public:
    int maxProfit(int k, vector<int>& prices)
    {
        int len = prices.size();
        if (len == 0 || k == 0) return 0;
        if (len < k) return maxProfit2(prices);

        vector<int> local(k + 1, 0);
        vector<int> global(k + 1, 0);
        int diff;
        for (int i = 0; i < len - 1; ++i)
        {
            diff = prices[i + 1] - prices[i];
            for (int j = k; j >= 1; --j)
            {
                local[j] = max(global[j - 1] + max(diff, 0), local[j] + diff);
                global[j] = max(local[j], global[j]);
            }
        }
        return global.back();
    }

    int maxProfit2(vector<int>& prices)
    {
        int profit = 0;
        for (int i = 0; i < prices.size() - 1; i++)
            profit = max(profit, profit + prices[i + 1] - prices[i]);
        return profit;
    }
};

int main()
{
    vector<int> prices{ 3,3,5,0,0,3,1,4 };
    cout << Solution{}.maxProfit(2, prices) << endl;
    getchar();
}
