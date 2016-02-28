#include <iostream>
using namespace std;

class Solution {
	int colculate_area(int A, int B, int C, int D) 
	{
		if (C - A <= 0 || D - B <= 0)
			return 0;
		return (C - A) * (D - B);
	}
public:
	int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
		int sum = colculate_area(A, B, C, D) + colculate_area(E, F, G, H);
		if (A > E)
		{
			swap(A, E);
			swap(B, F);
			swap(C, G);
			swap(D, H);
		}
		int left = E - A;
		int right = G - C;
		int top = H - D;
		int buttom = B - F;
		int switches = ((right > 0) << 2) + ((top > 0) << 1) + (buttom > 0);
		switch (switches)
		{
		case 0:
			sum -= colculate_area(E, F, G, H);
			break;
		case 1:
			sum -= colculate_area(E, B, G, H);
			break;
		case 2:
			sum -= colculate_area(E, F, G, D);
			break;
		case 3:
			sum -= colculate_area(E, B, G, D);
			break;
		case 4:
			sum -= colculate_area(E, F, C, H);
			break;
		case 5:
			sum -= colculate_area(E, B, C, H);
			break;
		case 6:
			sum -= colculate_area(E, F, C, D);
			break;
		case 7:
			sum -= colculate_area(E, B, C, D);
			break;
		}
		return sum;
	}
};

int main()
{
	cout << Solution{}.computeArea(-2, -2, 2, 2, 3, 3, 4, 4);
	getchar();
	return 0;
}