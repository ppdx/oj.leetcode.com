#include <iostream>
#include <vector>
#include <string>
#include <cstring>
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

void inorderTraversal(TreeNode *root, vector<int>& res)
{
    if (!root)
        return;
    inorderTraversal(root->left, res);
    res.push_back(root->val);
    inorderTraversal(root->right, res);
}

vector<int> inorderTraversal(TreeNode *root)
{
    vector<int> res;
    inorderTraversal(root, res);
    return res;
}

int main()
{
    const int size = 10;
    TreeNode nodes[size];
    for (size_t i = 0; i < size; i++)
        nodes[i].val = i;

    nodes[0].right = &nodes[1];
    nodes[1].left  = &nodes[2];
    for (int n : inorderTraversal(&nodes[0]))
        cout << n << ", ";
    system("pause");
    return 0;
}