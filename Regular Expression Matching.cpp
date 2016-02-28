#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

class Solution {
public:
	bool isMatch(const char *s, const char *p) {
		int height = strlen(s);
		int width = strlen(p);
		vector<vector<bool>> dp(height + 1, vector<bool>(width + 1, false));
		dp[0][0] = true;
		for (int i = 1; i <= width; i++)
		{
			if (p[i - 1] == '*')
			{
				dp[0][i] = dp[0][i - 2];
			}
		}
		for (int i = 1; i <= height; i++)
		{
			for (int j = 1; j <= width; j++)
			{
				char cs = s[i - 1];
				char cp = p[j - 1];
				if (cs == cp || cp == '*')
				{
					dp[i][j] = dp[i - 1][j - 1];
				}
				else if (cp == '*')
				{
					if (cs != p[j - 2] && p[j - 2] != '.')
					{
						dp[i][j] = dp[i][j - 2];
					}
					else
					{
						dp[i][j] = dp[i][j - 2] || dp[i - 1][j];
					}
				}
			}
		}
		return dp[height][width];

	}
};

int main()
{
	Solution ss;
	vector<pair<char*, char*>> v{ {"aa","a"},{"aa","aa"},{"aaa","a*a"},
	{"aa","a*"},{"aa",".*"},{"ab",".*"},{"aab","c*a*b*"} };
	for (auto p : v)
	{
		cout << p.first << " " << p.second << " " << ss.isMatch(p.first, p.second) << endl;
	}
}