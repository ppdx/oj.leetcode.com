#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
	int maximalSquare(vector<vector<char>>& matrix) {
		int row = matrix.size();
		if (row == 0) return 0;
		int col = matrix[0].size();

		vector<vector<char>> nums;
		for (int i = 0; i < row; i++)
		{
			vector<char> num(col, 0);
			num[col - 1] = matrix[i][col - 1] == '1';
			for (int j = col - 2; j >= 0; j--)
			{
				if (matrix[i][j] == '1')
					num[j] = num[j + 1] + 1;
				else
					num[j] = 0;
			}
			nums.push_back(move(num));
		}

		int max = 0;
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < col; j++)
			{
				int current = nums[i][j];
				if (current <= max || row - i <= max) continue;

				for (int k = current; k > max; k--)
				{
					bool flag = true;
					for (int l = i + 1; l < i + k; l++)
					{
						if (l >= row || nums[l][j] < k) { flag = false; break; }
					}
					if (flag){ max = k; break; }
				}
			}
		}
		return max*max;
	}
};

int main()
{
	vector<vector<char>> matrix{ { '1', '1' } };
	cout << Solution{}.maximalSquare(matrix) << endl;
	getchar();
}