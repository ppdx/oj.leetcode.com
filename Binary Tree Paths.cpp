class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        if (root == nullptr)
            return{};
        vector<string> res;
        string cur = to_string(root->val);
        if (root->left == nullptr&&root->right == nullptr)
            return{ cur };
        cur += "->";
        if (root->left)
        {
            auto l = binaryTreePaths(root->left);
            for (string& s : l)
                res.push_back(cur + s);
        }
        if (root->right)
        {
            auto r = binaryTreePaths(root->right);
            for (string& s : r)
                res.push_back(cur + s);
        }
        return res;
    }
};
