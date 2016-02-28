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
#include <unordered_set>
#include <numeric>
#include <cassert>
#include <array>
#include <utility>
using namespace std;


struct ListNode
{
    int val;
    ListNode* next;

    ListNode(int x) : val(x), next(nullptr)
    {}

    ListNode() : ListNode(0)
    {}
};

class Solution
{
public:
    ListNode* removeElements(ListNode* head, int val)
    {
        while (head && head->val == val)
            head = head->next;
        if (!head) return head;
        auto p = head;
        while (p->next)
        {
            if (p->next->val == val)
                p->next = p->next->next;
            else
                p = p->next;
        }
        return head;
    }
};

void print(ListNode* head)
{
    while (head)
    {
        cout << head->val;
        if (head->next)
            cout << " -> ";
        head = head->next;
    }
    cout << endl;
}

template <size_t len>
void init(ListNode(&d)[len], initializer_list<int> il)
{
    assert(len >= il.size());
    int i = 0;
    for (auto j = il.begin(); j != il.end(); ++i, ++j)
    {
        d[i].next = d + i + 1;
        d[i].val = *j;
    }
    d[il.size() - 1].next = nullptr;
}

int main()
{
    ListNode data[10];
    init(data, { 1,2,6,3,4,5,6 });
    print(data);
    Solution{}.removeElements(data, 6);
    print(data);
    getchar();
}
