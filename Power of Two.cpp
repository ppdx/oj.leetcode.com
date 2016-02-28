class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) return false;
        int count = 0;
        for (size_t i = 0; i < sizeof(int) * 8; i++)
        {
            if (n&(1 << i)) count += 1;
        }
        return count == 1;
    }
};
