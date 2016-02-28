class Solution {
public:
    int countDigitOne(int n) {
        if (n <= 0) return 0;
        else if (n < 10) return 1;
        int count = 0;
        int lower, heigh, current;
        long long factor = 1;
        while (n / factor)
        {
            lower = n % factor;
            heigh = n / factor / 10;
            current = (n / factor) % 10;
            switch (current)
            {
            case 0:
                count += heigh * factor;
                break;
            case 1:
                count += heigh * factor + lower + 1;
                break;
            default:
                count += (heigh + 1) * factor;
            }
            factor *= 10;
        }
        return count;
    }
};
