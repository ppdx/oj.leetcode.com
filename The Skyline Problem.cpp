#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> res;
        if (buildings.empty()) return res;
        map<int, vector<int>> border;
        for (auto& b : buildings) {
            border[b[0]].push_back(b[2]);
            border[b[1]].push_back(-b[2]);
        }
        multiset<int> heights{ 0 };
        for (auto& b : border) {
            for (int i : b.second)
                if (i < 0)
                    heights.erase(heights.find(-i));
                else
                    heights.insert(i);
            int c = *heights.rbegin();
            if (res.empty() || res.back().second != c)
                res.push_back(make_pair(b.first, c));
        }
        return res;
    }
};
