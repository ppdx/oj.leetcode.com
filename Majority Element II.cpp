class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int a1, a2, n1 = 0, n2 = 0;
        for (int i : nums)
        {
            if (n1 == 0 || a1 == i)
            {
                a1 = i;
                n1++;
            }
            else if (n2 == 0 || a2 == i)
            {
                a2 = i;
                n2++;
            }
            else
            {
                n1--;
                n2--;
            }
        }
        vector<int> res;
        if (count(begin(nums), end(nums), a1) > nums.size() / 3)
            res.push_back(a1);
        if (a1 != a2 && count(begin(nums), end(nums), a2) > nums.size() / 3)
            res.push_back(a2);
        return res;
    }
};
