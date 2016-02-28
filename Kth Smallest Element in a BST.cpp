class Solution {
    int count = 0;
    int k;
    void travel(TreeNode *root)
    {
        if (!root) return;
        travel(root->left);
        count++;
        if (count == k)
            throw root->val;
        travel(root->right);
    }
public:
    int kthSmallest(TreeNode* root, int k) {
        this->k = k;
        try
        {
            travel(root);
        }
        catch (int e)
        {
            return e;
        }
    }
};
