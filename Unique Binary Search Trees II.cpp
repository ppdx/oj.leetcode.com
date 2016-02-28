#include <iostream>
#include <vector>
#include <string>
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

void _clone(TreeNode* old_n, TreeNode* new_n)
{
    if (old_n->left)
    {
        new_n->left = new TreeNode(old_n->left->val);
        _clone(old_n->left, new_n->left);
    }

    if (old_n->right)
    {
        new_n->right = new TreeNode(old_n->right->val);
        _clone(old_n->right, new_n->right);
    }
}

TreeNode* clone(TreeNode* node)
{
    if (!node)
        return NULL;
    auto root = new TreeNode(node->val);
    _clone(node, root);
    return root;
}

void dispose(TreeNode* root)
{
    if (!root)
        return;
    dispose(root->left);
    dispose(root->right);
    delete root;
}
const vector<TreeNode*> NoneNode{ NULL };
vector<TreeNode*> generateNode(int left, int right)
{
    if (left > right)
        return NoneNode;
    if (left == right)
        return vector<TreeNode*>{new TreeNode{ left }};
    vector<TreeNode*> res;
    for (int i = left; i <= right; i++)
    {
        auto l = generateNode(left, i - 1);
        auto r = generateNode(i + 1, right);

        for (auto a : l)
            for (auto b : r)
            {
                auto root = new TreeNode(i);
                root->left = clone(a);
                root->right = clone(b);
                res.push_back(root);
            }

        for (auto a : l)
            dispose(a);
        for (auto b : r)
            dispose(b);
    }
    return res;
}

vector<TreeNode *> generateTrees(int n)
{
    return generateNode(1, n);
}

int main()
{
    auto r = generateTrees(3);
    return 0;
}