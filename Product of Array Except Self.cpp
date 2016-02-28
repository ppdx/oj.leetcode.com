class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res = nums;
        if (nums.size() == 0) return res;
        int tmp = 1;
        for (size_t i = 0; i < nums.size(); i++)
        {
            res[i] = tmp;
            tmp *= nums[i];
        }
        tmp = 1;
        for (int i = nums.size() - 1; i >= 0; i--)
        {
            res[i] *= tmp;
            tmp *= nums[i];
        }
        return res;
    }
};
