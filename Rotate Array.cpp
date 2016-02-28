#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
using namespace std;

void rotate(int nums[], int n, int k)
{
    if (n == 0 || n == 1 || k == 0)
        return;
    reverse(nums, nums + n - k);
    reverse(nums + n - k, nums + n);
    reverse(nums, nums + n);
}

int main()
{
    vector<int> a{ 1,2,3,4,5,6,7 };
    rotate(&a[0], 2, 1);
    for (size_t i = 0; i < a.size(); i++)
    {
        cout << a[i] << " ";
    }
    system("pause");
    return 0;
}