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

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr)
    {}
    TreeNode(int x, TreeNode* l, TreeNode* r) :val(x), left(l), right(r)
    {}
    TreeNode() : TreeNode(count++)
    {}
    static int count;
};
int TreeNode::count = 0;

class Solution
{
public:
    int maxPathSum(TreeNode *root)
    {
        max_sum = numeric_limits<int>::min();
        helper(root);
        return max_sum;
    }
private:
    int max_sum;
    int helper(TreeNode* root)
    {
        if (!root) return 0;
        int left = helper(root->left);
        int right = helper(root->right);
        int ssum = root->val + max(left, right);
        max_sum = max(max_sum, root->val + left + right);
        return max(ssum,0);
    }
};

#define cl(a,b) d[a].left = &d[b]
#define cr(a,b) d[a].right = &d[b]
int main()
{
    TreeNode d[10];
    d[1].val = -3;
    cout << Solution{}.maxPathSum(d + 1) << endl;
    getchar();
}