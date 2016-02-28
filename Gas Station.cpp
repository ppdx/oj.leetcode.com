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

// ³¬Ê±¡£¡£¡£
//int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
//{
//	size_t len = gas.size();
//	vector<int> prefit(len);
//	int allprefit = 0;
//	for (size_t i = 0; i < len; i++)
//	{
//		prefit[i] = gas[i] - cost[i];
//		allprefit += prefit[i];
//	}
//	if (allprefit < 0)
//		return -1;
//
//	for (size_t i = 0; i < len; i++)
//	{
//		int current = prefit[i];
//		for (size_t j = i + 1; j < len; j++)
//		{
//			if (current < 0)
//				goto next_start_station;
//			current += prefit[j];
//		}
//		for (size_t j = 0; j < i; j++)
//		{
//			if (current < 0)
//				goto next_start_station;
//			current += prefit[j];
//		}
//		return i;
//next_start_station:;
//	}
//
//	for (size_t i = 0; i < len; i++)
//		prefit[i] = gas[i] - (i == 0 ? cost.back() : cost[i - 1]);
//
//	for (int i = len - 1; i >= 0; i--)
//	{
//		int current = prefit[i];
//		for (int j = i - 1; j >= 0; j--)
//		{
//			if (current < 0)
//				goto next_start_station1;
//			current += prefit[j];
//		}
//		for (int j = len - 1; j > i; j--)
//		{
//			if (current < 0)
//				goto next_start_station1;
//			current += prefit[j];
//		}
//		return i;
//next_start_station1:;
//	}
//	return -1;
//}

int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
{
	int sum = 0;
	int total = 0;
	int j = -1;
	for (int i = 0; i < gas.size(); ++i)
	{
		sum += gas[i] - cost[i];
		total += gas[i] - cost[i];
		if (sum < 0)
		{
			j = i; 
			sum = 0;
		}
	}
	if (total < 0) return -1;
	else return j + 1;
}

int main()
{
	vector<int> gas{ 1, 2, 3 };
	vector<int> cost{ 2, 1, 2 };
	cout << canCompleteCircuit(gas, cost) << endl;
	system("pause");
	return 0;
}