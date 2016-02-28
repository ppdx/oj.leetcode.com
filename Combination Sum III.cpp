class Solution {
public:
    vector<vector<int>> helper(int k, int n, int start)
    {
        vector<vector<int>> res;
        if (n / k > 9) return res;
        if (k == 1) {
            res.push_back(vector<int>{n});
            return res;
        }
        for (int i = start; i <= (k == 2 && n % 2 == 0 ? n / k - 1 : n / k); i++)
        {
            auto tail = helper(k - 1, n - i, i + 1);
            if (!tail.empty())
                for (auto& v : tail)
                {
                    v.insert(v.begin(), i);
                    res.push_back(move(v));
                }
        }
        return res;
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        return helper(k, n, 1);
    }
};
