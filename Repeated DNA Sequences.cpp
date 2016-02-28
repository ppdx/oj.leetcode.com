#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <iterator>
using namespace std;

/************************ 1 超内存 *************************/
vector<string> findRepeatedDnaSequences1(string s)
{
    if (s.length() <= 10)
        return vector<string>();
    unordered_map<string, int> all;
    unordered_map<string, int> repeat;

    for (size_t i = 0; i < s.length() - 9; i++)
    {
        string current = s.substr(i, 10);
        if (all.find(current) == all.end())
            all[current] = 1;
        else
            repeat[current] = 1;
    }
    vector<string> ret;
    for (auto i = repeat.begin(); i != repeat.end(); i++)
        ret.push_back(i->first);
    return ret;
}

/*************************** 2 ****************************/
int toInt(char c)
{
    switch (c)
    {
    case 'A':
        return 0;
    case 'T':
        return 1;
    case 'G':
        return 2;
    case 'C':
        return 3;
    }
}

// 使用两位保存一个DNA位
int toIndentfy(string& s, int start)
{
    int ret = 0;
    for (size_t i = 0; i < 10; i++, ret <<= 2)
    {
        ret += toInt(s[start + i]);
    }
    return ret;
}

vector<string> findRepeatedDnaSequences2(string s)
{
    if (s.length() <= 10)
        return vector<string>();
    unordered_map<int, int> all;
    vector<string> ret;

    for (size_t i = 0; i < s.length() - 9; i++)
    {
        int current = toIndentfy(s, i);
        if (all.find(current) == all.end())
            all[current] = 1;
        else
        {
            if (all[current] == 1)
                ret.push_back(s.substr(i, 10));
            all[current] += 1;
        }
    }
    return ret;
}

/*************************** 3 ****************************/
vector<string> findRepeatedDnaSequences(string s)
{
    size_t len = s.length();
    if (len <= 10)
        return vector<string>();

    unordered_map<int, int> all;
    vector<string> ret;
    const int mark20 = 0xfffff;
    int table['Z'];
    table['A'] = 0;
    table['T'] = 1;
    table['G'] = 2;
    table['C'] = 3;

    int current = 0;
    for (size_t i = 0; i < 9; i++)
    {
        current <<= 2;
        current += table[s[i]];
    }

    for (size_t i = 9; i < len; i++)
    {
        current = ((current << 2) + table[s[i]]) & mark20;
        if (all.find(current) == all.end())
            all[current] = 1;
        else
        {
            if (all[current] == 1)
                ret.push_back(s.substr(i - 9, 10));
            all[current] += 1;
        }
    }
    return ret;
}
int main()
{
    string str = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
    cout << str << endl;
    auto ret = findRepeatedDnaSequences(str);
    for (auto& s : ret)
        cout << s << endl;
    system("pause");
    return 0;
}