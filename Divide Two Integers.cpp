#include <iostream>
#include <limits>
using namespace std;

class Solution {
public:
	int divide(int dividend, int divisor) {
		if (divisor == 0)
		{
			return numeric_limits<int>::max();
		}
		if (dividend == divisor)
		{
			return 1;
		}
		if (divisor == 1)
		{
			return dividend;
		}
		if (divisor == numeric_limits<int>::min())
		{
			return 0;
		}
		int result = 0;
		if (dividend == numeric_limits<int>::min())
		{
			if (divisor == -1)
			{
				return numeric_limits<int>::max();
			}
			else
			{
				dividend += labs(divisor);
				result += 1;
			}
		}
		if (divisor == 0)
		{
			return 0;
		}

		int sign = 1;
		if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor>0))
		{
			sign = -1;
		}
		dividend = labs(dividend);
		divisor = labs(divisor);
		int bitsOfDivisor = 0;
		while (divisor >> bitsOfDivisor != 0)
		{
			bitsOfDivisor++;
		}
		int bitsOfDividend = 0;
		while (dividend >> bitsOfDividend != 0)
		{
			bitsOfDividend++;
		}
		for (int i = bitsOfDividend - bitsOfDivisor; i >= 0; i--)
		{
			if (dividend >= (divisor << i))
			{
				dividend -= (divisor << i);
				result += 1 << i;
			}
		}
		return result*sign;
	}
};

int main() {
	Solution sol;
	int a, b;
	while (1) {
		cin >> a >> b;
		cout << sol.divide(a, b) << endl;
	}
}