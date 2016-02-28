#include <iostream>
using namespace std;

class Solution {
public:
    double pow(double x, int n) {
        if(n==0)
            return 1;
        else if(n>0)
            return _pow(x,n);
        else
            return _pow(1/x,-n);
    }
    double _pow(double x,int n) {
        if(n==0)
            return 1;
        double a=_pow(x,n/2);
        return a*a*(n%2==1?x:1);
    }
};

int main() {
    Solution sol;
    cout<< sol.pow(34.00515, -3)<<endl;
}
