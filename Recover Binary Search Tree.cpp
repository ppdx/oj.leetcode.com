class Solution {
    TreeNode *n1, *n2, *pre;
public:
    void helper(TreeNode* root)
    {
        if (!root) return;
        helper(root->left);
        if (pre && pre->val > root->val)
        {
            if (!n1) n1 = pre;
            n2 = root;
        }
        pre = root;
        helper(root->right);
    }

    void recoverTree(TreeNode* root) {
        if (!root) return;
        n1 = n2 = pre = nullptr;
        helper(root);
        swap(n1->val, n2->val);
    }
};
