#include <iostream>
#include <vector>
#include <string>
#include <limits>
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

//inline int min(int a, int b, int c)
//{
//    return a < b ? (a < c ? a : c) : (b < c ? b : c);
//}
//inline int max(int a, int b, int c)
//{
//    return a > b ? (a > c ? a : c) : (b > c ? b : c);
//}
//pair<int, int> search(TreeNode *root)
//{
//    if (!root)
//        return make_pair(numeric_limits<int>::min(), numeric_limits<int>::max());
//    auto left = search(root->left);
//    auto right = search(root->right);
//    if (left.first < root->val && right.second > root->val)
//        return make_pair(max(left.first, right.first, root->val),
//        min(left.second, right.second, root->val));
//    throw string{ "lalala" };
//}
//
//bool isValidBST(TreeNode *root)
//{
//    try
//    {
//        search(root);
//    }
//    catch (string)
//    {
//        return false;
//    }
//    return true;
//}

//bool isBSTRec(TreeNode* root, int left, int right)
//{
//    if (root == NULL)
//    {
//        return true;
//    }
//    if (root->val <= left || root->val >= right)
//    {
//        return false;
//    }
//
//    return isBSTRec(root->left, left, root->val) && isBSTRec(root->right, root->val, right);
//}
//
//bool isValidBST(TreeNode* root)
//{
//    return isBSTRec(root, numeric_limits<int>::min(), numeric_limits<int>::max());
//}

bool isValidBST(TreeNode* root)
{
    static TreeNode* prev = NULL;

    // traverse the tree in inorder fashion and keep track of prev node
    if (root)
    {
        if (!isValidBST(root->left))
            return false;

        // Allows only distinct valued nodes 
        if (prev != NULL && root->val <= prev->val)
            return false;

        prev = root;

        return isValidBST(root->right);
    }

    return true;
}

int main()
{
    const char* str = "2147483647";
    const int size = 10;
    TreeNode nodes[size];
    for (size_t i = 0; i < size; i++)
        nodes[i].val = str[i];

    //nodes[0].left = &nodes[1];
    //nodes[0].right = &nodes[2];
    //nodes[1].left = &nodes[3];
    //nodes[1].right = &nodes[4];
    //nodes[2].left = &nodes[5];
    //nodes[2].right = &nodes[6];
    //nodes[3].left = &nodes[7];
    //nodes[3].right = &nodes[8];
    //nodes[4].left = &nodes[9];

    nodes[0].left = &nodes[1];
    nodes[1].val = -1;
    cout << isValidBST(&nodes[0]) << endl;
    system("pause");
    return 0;
}