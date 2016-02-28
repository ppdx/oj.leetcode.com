class Solution {
    vector<int> nums;
    vector<char> operates;
public:
    vector<int> diffWaysToCompute(string input) {
        parse(input);
        if (operates.size() == 0)
            return nums;
        return comput(0, operates.size() - 1);
    }
    vector<int> comput(int left, int right)
    {
        if (left > right)
            return{ nums[left] };
        if (left == right)
            return{ calculate(nums[left], nums[left + 1], operates[left]) };
        vector<int> res;
        for (int i = left; i <= right; i++)
        {
            auto l = comput(left, i - 1);
            auto r = comput(i + 1, right);
            for (int x : l)
                for (int y : r)
                    res.push_back(calculate(x, y, operates[i]));
        }
        return res;
    }
    int calculate(int a, int b, int op)
    {
        switch (op)
        {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        }
    }
    void parse(string& input)
    {
        istringstream iss(input);
        int num; char operate;
        iss >> num;
        nums.push_back(num);
        while (!iss.eof())
        {
            iss >> operate >> num;
            operates.push_back(operate);
            nums.push_back(num);
        }
    }
};
