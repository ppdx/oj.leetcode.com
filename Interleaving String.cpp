#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// 以下算法超时。。。
bool isInterleave1(string s1, string s2, string s3)
{
    if (s1.length() + s2.length() != s3.length())
        return false;

    vector<const char*> s;
    const char * a = s1.c_str();
    const char * b = s2.c_str();
    const char * c = s3.c_str();

    while (*c)
    {
        if (*a == *c)
        {
            if (*b == *c)
            {
                s.push_back(a);
                s.push_back(b + 1);
                s.push_back(c);
            }
            a += 1;
        }
        else
        {
            if (*b == *c)
                b += 1;
            else
            {
                if (s.size() == 0)
                    return false;

                c = s.back();
                s.pop_back();

                b = s.back();
                s.pop_back();

                a = s.back();
                s.pop_back();
            }
        }
        c++;
    }
    return true;
}

bool isInterleave(string s1, string s2, string s3)
{
    int row = s1.length();
    int column = s2.length();
    int len = s3.length();
    if (row + column != len)
        return false;
    if ((row == 0 && s2 == s3) || (column == 0 && s1 == s3))
        return true;
    vector<vector<char>> dp(row + 1, vector<char>(column + 1, 0));

    for (int i = 0; i < row; i++)
        dp[i + 1][0] = (s1[i] == s3[i]);
    for (int i = 0; i < column; i++)
        dp[0][i + 1] = (s2[i] == s3[i]);
    
    for (int i = 1; i <= row; i++)
        for (int j = 1; j <= column; j++)
        {
            if ((dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) 
                || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]))
                dp[i][j] = 1;
        }
    return dp[row][column];
}

int main()
{
    string s1 = "";
    string s2 = "";
    string s3 = "";

    cout << s1 << endl;
    cout << s2 << endl;
    cout << s3 << endl;
    cout << isInterleave(s1, s2, s3) << endl;

    system("pause");
    return 0;
}