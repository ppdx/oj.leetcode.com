class Solution {
    TreeNode* p, *q;
    bool trival(TreeNode* root)
    {
        if (!root) return false;
        int sum = (root == p) + (root == q) + trival(root->left) + trival(root->right);
        if (sum == 2)
            throw root;
        return sum == 1;
    }
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        this->p = p;
        this->q = q;
        try
        {
            trival(root);
        }
        catch (TreeNode* t)
        {
            return t;
        }
        return root;
    }
};
