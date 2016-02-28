#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    int get_left(TreeNode* root) {
        int h = 1;
        while (root = root->left)
            h++;
        return h;
    }

    int get_right(TreeNode* root) {
        int h = 1;
        while (root = root->right)
            h++;
        return h;
    }
public:
    int countNodes(TreeNode* root) {
        if (!root) return 0;
        int left = get_left(root);
        int right = get_right(root);
        if (left == right)
            return (1 << left) - 1;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
