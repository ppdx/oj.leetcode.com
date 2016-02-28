#include <iostream>
#include <string>
using namespace std;

int titleToNumber(string s)
{
    int r=0;
    for(int i=0; i<s.length(); i++)
    {
        r*=26;
        r+=s[i]-'A'+1;
    }
    return r;
}

int main()
{
    string s="AB";
    cout<<s<<" = "<<titleToNumber(s)<<endl;
    return 0;
}
