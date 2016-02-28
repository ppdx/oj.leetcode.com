class Solution {
public:
    string summary(int left, int right) {
        string s;
        if (left != right)
            s.append(to_string(left)).append("->").append(to_string(right));
        else
            s.append(to_string(left));
        return s;
    }

    vector<string> summaryRanges(vector<int>& nums) {
        int length = nums.size();
        if (length == 0) return vector<string>{};
        else if (length == 1) return vector<string>{to_string(nums[0])};

        vector<string> res;
        int last = nums[0];
        for (int i = 1; i < length; i++)
        {
            if (nums[i] - nums[i - 1] == 1)
                continue;
            res.push_back(summary(last, nums[i - 1]));
            last = nums[i];
        }
        res.push_back(summary(last, nums.back()));
        return res;
    }
};
