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
using namespace std;
/** 1 **/
class Solution1
{
    struct state
    {
        int current, min;
        state operator+(int n)
        {
            state ret{ current + n, 0 };
            ret.min = ret.current < min ? ret.current : min;
            return ret;
        }
    };

public:
    int calculateMinimumHP(vector<vector<int> > &dungeon)
    {
        if (dungeon.empty() || dungeon[0].empty()) return 1;
        int row = dungeon.size();
        int column = dungeon[0].size();
        vector<state> last(column,
                           state{ numeric_limits<int>::min(), numeric_limits<int>::min() });
        last[0] = state{ 0, 0 };
        vector<state> now(column);
        for (int i = 0; i < row; i++)
        {
            now[0] = last[0] + dungeon[i][0];
            for (int j = 1; j < column; j++)
            {
                now[j] = now[j - 1] + dungeon[i][j];
                last[j] = last[j] + dungeon[i][j];
                if (last[j].min > now[j].min)
                    now[j] = last[j];
            }
            swap(now, last);
        }
        return last.back().min <= 0 ? 1 - last.back().min : last.back().min;
    }
};

/** 2 **/
class Solution
{
public:
    int calculateMinimumHP(vector<vector<int> > &dungeon)
    {
        int m = dungeon.size();
        int n;
        if (m == 0)
            return 0;
        else
            n = dungeon[0].size();
        vector<int> minHP(n, 0);
        for (int i = m - 1; i >= 0; i--)
        {
            for (int j = n - 1; j >= 0; j--)
            {
                if (i == m - 1 && j == n - 1) // bottom-right one
                    minHP[j] = 1 - dungeon[i][j];
                else if (i == m - 1)         // last row
                    minHP[j] = minHP[j + 1] - dungeon[i][j];
                else if (j == n - 1)         // last col
                    minHP[j] = minHP[j] - dungeon[i][j];
                else
                    minHP[j] = min(minHP[j], minHP[j + 1]) - dungeon[i][j]; // others
                if (minHP[j] <= 0)    // insure have one
                    minHP[j] = 1;
            }
        }
        return minHP[0];
    }
};

int main()
{
    default_random_engine generator;
    uniform_int_distribution<int> distribution(1, 100);
    auto rand_size = bind(distribution, generator);
    uniform_int_distribution<int> distribution2(-100, 100);
    auto rand_data = bind(distribution2, generator);

    int correct = 0;
    int wrong = 0;

    for (int i = 0; i < 100; i++)
    {
        vector<vector<int>> data(rand_size(), vector<int>(rand_size()));
        for (auto& row : data)
            for (auto& ceil : row)
                ceil = rand_data();
        int result1 = Solution1{}.calculateMinimumHP(data);
        int result2 = Solution{}.calculateMinimumHP(data);
        if (result1 != result2)
        {
            cout << "data:" << endl;
            for (auto& row : data)
            {
                for (auto& ceil : row)
                    cout << ceil << " ";
                cout << endl;
            }
            cout << "standard : " << result2 << endl;
            cout << "my : " << result1 << endl;
			cout << "------------------------------------" << endl << endl;
        }
    }
    system("pause");
    return 0;
}
