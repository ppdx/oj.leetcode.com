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
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr)
    {}
    TreeNode(int x, TreeNode* l, TreeNode* r) :val(x), left(l), right(r)
    {}
    TreeNode() :TreeNode(count++)
    {}
    static int count;
};
int TreeNode::count = 0;

class Solution
{
    vector<int> view;
public:
    vector<int> rightSideView(TreeNode *root)
    {
        viewTree(root, 0);
        return view;
    }

    void viewTree(TreeNode* root, int level)
    {
        if (root == nullptr)return;
        if (view.size() == level)
            view.push_back(0);
        viewTree(root->left, level + 1);
        view[level] = root->val;
        viewTree(root->right, level + 1);
    }
};

#define cl(a,b) d[a].left = &d[b]
#define cr(a,b) d[a].right = &d[b]
int main()
{
    TreeNode d[10];
    cl(1, 2);
    for (auto i : Solution{}.rightSideView(&d[1]))
        cout << i << " ";
}