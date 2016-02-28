#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution
{
    vector<vector<string> > result;
public:
    vector<vector<string> > solveNQueens(int n)
    {
        vector<int> state;
        for (int i = 0; i < n; i++)
        {
            state.push_back(i);
        }
        vector<string> cur(n, string(n, '.'));
        while (true)
        {
            if (check(state,n))
            {
                for (int i = 0; i < n; i++)
                {
                    cur[i][state[i]] = 'Q';
                }
                result.push_back(cur);
                for (int i = 0; i < n; i++)
                {
                    cur[i][state[i]] = '.';
                }
            }
            if (!next_permutation(begin(state), end(state)))
            {
                break;
            }
        }
        return result;
    }

    bool check(const vector<int> &state,int n)
    {
        int j;
        for (int i = 0; i < n; i++)
        {
            j = 1;
            while (i + j < n)
            {
                if (state[i + j] == state[i] + j || state[i + j] == state[i] - j)
                {
                    return false;
                }
                j++;
            }
        }
        return true;
    }
};

int main()
{
    Solution().solveNQueens(9);
}