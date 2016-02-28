/*
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
*/

#include <iostream>
#include <cstdio>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

class Solution {
	int number;
public:
	int calculate(string s) {
		istringstream iss{ s };
		vector<int> stack = { 0 };
		bool is_add = true;
		int token;
		while (token = get_token(iss))
		{
			switch (token)
			{
			case '+':
			case '-':
				is_add = token == '+';
				break;
			case '(':
				stack.push_back(is_add);
				is_add = true;
				stack.push_back(0);
				break;
			case ')':
				number = stack.back();
				stack.pop_back();
				is_add = static_cast<bool>(stack.back());
				stack.pop_back();
			case 1:
				if (is_add)
					stack.back() += number;
				else
					stack.back() -= number;
				break;
			}
		}
		return stack.back();
	}

	int get_token(istringstream &iss)
	{
		char c = ' ';
		while (!iss.eof() && c == ' ')
			iss >> c;
		if (c <= '9' && c >= '0')
		{
			iss.putback(c);
			iss >> number;
			c = 1;
		}
		return c == ' ' ? 0 : c;
	}
};

int main()
{
	string tast[]{ "1 + 1", " 2-1 + 2 ", "(1+(4+5+2)-3)+(6+8)", "1-(5)"};
	int result[]{2, 3, 23};
	for (int i = 0; i < sizeof(tast) / sizeof(string); i++)
	{
		cout << "eval(\"" << tast[i] << "\") = " << Solution{}.calculate(tast[i]) << endl;
	}
	getchar();
	return 0;
}
