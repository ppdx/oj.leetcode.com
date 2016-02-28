class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        unordered_set<int> data;
        for (int i : nums)
            if (data.count(i)) data.erase(i); else data.insert(i);
        return{ data.begin(), data.end() };
    }
};
