class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int j = matrix[0].size();
        for (auto i = matrix.begin(); i != matrix.end() && (*i)[0] <= target; ++i)
        {
            auto iter = lower_bound(i->begin(), i->begin() + j, target);
            if (iter == i->end()) continue;
            if (*iter == target) return true;
            j = iter - i->begin();
        }
        return false;
    }
};
