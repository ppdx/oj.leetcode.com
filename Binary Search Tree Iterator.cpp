#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : TreeNode(0) {}
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    TreeNode(int x, TreeNode* l, TreeNode* r) : val(x), left(l), right(r) {}
};

class BSTIterator
{
    enum class station
    {
        L, M, R
    };
    TreeNode *_root;
    vector < pair<TreeNode*, station> > stack;
public:
    BSTIterator(TreeNode *root) : _root(root), stack{  }
    {
        stack.push_back(make_pair(root, station::L));
    }

    /** @return whether we have a next smallest number */
    bool hasNext()
    {
        while (!stack.empty())
        {
            auto current = stack.back();
            if (current.first == nullptr)
            {
                stack.pop_back();
                continue;
            }
            switch (current.second)
            {
            case station::L:
                stack.back().second = station::M;
                stack.push_back(make_pair(current.first->left, station::L));
                break;
            case station::M:
                return true;
            case station::R:
                stack.pop_back();
                stack.push_back(make_pair(current.first->right, station::L));
                break;
            }
        }
        return false;
    }

    /** @return the next smallest number */
    int next()
    {
        auto& current  = stack.back();
        current.second = station::R;
        return current.first->val;
    }
};

int main()
{
    const int size = 10;
    TreeNode nodes[size];
    for (size_t i = 0; i < size; i++)
        nodes[i].val = i;

    nodes[0].right = &nodes[1];
    nodes[1].right = &nodes[2];
    BSTIterator bst{ &nodes[0] };
    while (bst.hasNext())
    {
        cout << bst.next() << endl;
    }
    system("pause");
    return 0;
}