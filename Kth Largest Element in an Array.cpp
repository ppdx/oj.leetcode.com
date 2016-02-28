#include <algorithm>
#include <iostream>
#include <vector>
#include <limits>
using namespace std;

template<typename T>
void print(T v){
    for(auto& i:v)
        cout<<i<<' ';
    cout<<endl;
}

class Solution
{
public:
    int findKthLargest(vector<int>& nums, int k)
    {
        vector<int> heap(k,numeric_limits<int>::min());
        for(auto i:nums)
        {
            if(heap.front()>i) continue;
            heap.front()=i;
            make_heap(heap.begin(),heap.end(),greater<int>{});
        }
        sort_heap(heap.begin(),heap.end(),greater<int>{});
        return heap.back();
    }
};

int main()
{
    vector<int> nums{-1,2,0};
    int k=3;
    cout<<Solution{}.findKthLargest(nums,k)<<endl;
}
