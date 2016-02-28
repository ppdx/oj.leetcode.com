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

bool isHappy(int n)
{
    unordered_set<int> view;
    while (view.find(n) == view.end() && n != 1)
    {
        view.insert(n);
        int sum = 0;
        while (n > 0)
        {
            sum += pow(n % 10, 2);
            n /= 10;
        }
        n = sum;
    }
    return n == 1;
}

int main()
{
    cout << isHappy(19) << endl;
    getchar();
}