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
#include <map>
using namespace std;

//class MinStack
//{
//	map<int, int> nums;
//	vector<int> stack;
//public:
//	void push(int x)
//	{
//		stack.push_back(x);
//		if (nums.find(x) == nums.end())
//			nums[x] = 1;
//		else
//			nums[x] += 1;
//	}
//
//	void pop()
//	{
//		int last = stack.back();
//		if (nums[last] == 1)
//			nums.erase(last);
//		else
//			nums[last] -= 1;
//		stack.pop_back();
//	}
//
//	int top()
//	{
//		return stack.back();
//	}
//
//	int getMin()
//	{
//		return nums.cbegin()->first;
//	}
//};

class MinStack
{
	struct val_min
	{
		int val, min;
	};
	vector<val_min> stack;
public:
	MinStack() :stack{}
	{
		stack.push_back(val_min{ 0, numeric_limits<int>::max() });
	}
	void push(int x)
	{
		if (x < stack.back().min)
			stack.push_back(val_min{ x, x });
		else
			stack.push_back(val_min{ x, stack.back().min });
	}

	void pop()
	{
		stack.pop_back();
	}

	int top()
	{
		return stack.back().val;
	}

	int getMin()
	{
		return stack.back().min;
	}
};

int main()
{
	MinStack ms{};
	for (int i = 0; i < 1000; i++)
	{
		ms.push(999 - i);
	}
	for (int i = 0; i < 1000; i++)
	{
		if (ms.getMin() != i)
		{
			cout << "help" << endl;
		}
		ms.pop();
	}
	system("pause");
	return 0;
}