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
using namespace std;

struct UndirectedGraphNode
{
    int label;
    vector<UndirectedGraphNode *> neighbors;
    UndirectedGraphNode(int x) : label(x)
    {};
    UndirectedGraphNode() : label(count)
    {
        count++;
    }
    static int count;
};
int UndirectedGraphNode::count = 0;

class Solution
{
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node)
    {
        if (node == nullptr)
            return node;
        unordered_set<UndirectedGraphNode*> visited;
        unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> conn;

        UndirectedGraphNode* res = new UndirectedGraphNode(node->label);
        vector<UndirectedGraphNode*> stack(node->neighbors.begin(), node->neighbors.end());
        conn[node] = res;
        visited.insert(node);
        for (auto p : node->neighbors)
        {
            if (conn.find(p) == conn.end())
                conn[p] = new UndirectedGraphNode(p->label);
            res->neighbors.push_back(conn[p]);
            if (visited.find(p) == visited.end())
                stack.push_back(p);
        }

        while (!stack.empty())
        {
            auto cur = stack.back();
            stack.pop_back();
            if (visited.find(cur) != visited.end())
                continue;
            visited.insert(cur);
            if (conn.find(cur) == conn.end())
                conn[cur] = new UndirectedGraphNode(cur->label);
            auto now = conn[cur];
            for (auto p : cur->neighbors)
            {
                if (conn.find(p) == conn.end())
                    conn[p] = new UndirectedGraphNode(p->label);
                now->neighbors.push_back(conn[p]);
                if (visited.find(p) == visited.end())
                    stack.push_back(p);
            }
        }
        return res;
    }
};

ostream& operator<<(ostream& os, UndirectedGraphNode* node)
{
    os << node->label << " : ";
    for (auto p : node->neighbors)
        os << p->label << ' ';
    return os;
}

void printMap(UndirectedGraphNode *node)
{
    unordered_set<UndirectedGraphNode*> visited;

    function<void(UndirectedGraphNode*)> visit = [&](UndirectedGraphNode* node)
    {
        if (visited.find(node) != visited.end())
            return;
        visited.insert(node);
        cout << node << endl;
        for (auto p : node->neighbors)
            visit(p);
    };
    visit(node);
}

int main()
{
    UndirectedGraphNode data[10];
    auto list = [&data](initializer_list<int> ll)
    {
        vector<UndirectedGraphNode*> res;
        for (auto i : ll)
            res.push_back(data + i);
        return res;
    };
    data[0].neighbors = list({ 0,0 });
    printMap(data);
    cout << "---------------------------------" << endl;
    printMap(Solution{}.cloneGraph(data));
    system("pause");
}