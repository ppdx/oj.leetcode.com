class Solution {
public:
    int addDigits(int num) {
        int r = 0;
        while (num > 9)
        {
            while (num)
            {
                r += num % 10;
                num /= 10;
            }
            num = r;
            r = 0;
        }
        return num;
    }
};
