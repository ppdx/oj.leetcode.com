#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int numTrees(int n)
{
    vector<int> dp(n + 1);
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        for (int j = 0; j < i; j++)
            dp[i] += dp[j] * dp[i - j - 1];
    }
    return dp[n];
}

int main()
{
    cout << numTrees(3) << endl;
    system("pause");
    return 0;
}