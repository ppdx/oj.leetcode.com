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
    int numIslands(vector<vector<char>> &grid)
    {
        int row = grid.size();
        if (row == 0) return 0;
        int col = grid[0].size();
        int res = 0;
        vector<vector<char>> visited(row, vector<char>(col, 0));
        vector<pair<int, int>> stack;
        int x, y;
        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
            {
                if (grid[i][j] == '0' || visited[i][j])
                    continue;
                res++;
                stack.push_back(make_pair(i, j));
                while (!stack.empty())
                {
                    tie(x, y) = stack.back();
                    stack.pop_back();
                    visited[x][y] = 1;
                    if (x > 0 && grid[x - 1][y] == '1' && !visited[x - 1][y])
                        stack.push_back(make_pair(x - 1, y));
                    if (y > 0 && grid[x][y - 1] == '1' && !visited[x][y - 1])
                        stack.push_back(make_pair(x, y - 1));
                    if (x < row - 1 && grid[x + 1][y] == '1' && !visited[x + 1][y])
                        stack.push_back(make_pair(x + 1, y));
                    if (y < col - 1 && grid[x][y + 1] == '1' && !visited[x][y + 1])
                        stack.push_back(make_pair(x, y + 1));
                }
            }
        return res;
    }
};

int main()
{
    vector<vector<char>> test1{ { '1','1','1','1','0' },
        { '1','1','0','1','0' },
        { '1','1','0','0','0' },
        { '0','0','0','0','0' } };
    vector<vector<char>> test2{ { '1','1','0','0','0' },
        { '1','1','0','0','0' },
        { '0','0','1','0','0' },
        { '0','0','0','1','1' }, };
    cout << Solution{}.numIslands(test1) << endl;
    cout << Solution{}.numIslands(test2) << endl;
    getchar();
}