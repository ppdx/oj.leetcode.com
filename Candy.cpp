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
using namespace std;

int candy(vector<int>& ratings)
{
    int len = ratings.size();
    vector<int> num(len, 1);
    for (int i = 1; i < len; i++)
        if (ratings[i] > ratings[i - 1])
            num[i] = num[i - 1] + 1;
    for (int i = len - 2; i >= 0; i--)
        if (ratings[i] > ratings[i + 1] && num[i] <= num[i + 1])
            num[i] = num[i + 1] + 1;
    return accumulate(num.begin(), num.end(), 0);
}

int main()
{
    vector<int> ratings{1,2,2};
    cout << candy(ratings) << endl;
    system("pause");
    return 0;
}
