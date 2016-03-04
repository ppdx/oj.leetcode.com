#include "stdafx.h"

int main()
{
	//vector<pair<int, int>> vp{ 10, pair<int,int>{1,2} };
	//cout << "VP: " << vp << endl;

	//initializer_list<int> il = { 1,2,3,4,5 };
	//auto ll = make_linkedlist(il.begin(), il.end());
	//cout << "ll: " << ll << endl;

	for (auto s : { "[]","[1,2,3]","[1,null,2,3]","[5,4,7,3,null,2,null,-1,null,9]" })
	{
		auto node = deserialize(s);
		cout << s << " -> " << node << endl;
		cout << serialize(node) << endl;
	}


	system("pause");
}