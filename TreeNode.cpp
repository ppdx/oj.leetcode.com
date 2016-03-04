#include "stdafx.h"

ostream& operator<< (ostream& os, TreeNode* node)
{
	if (node == nullptr) return os << "null";
	return os << "TreeNode(" << node->val << ", "
		<< node->left << ", " << node->right << ")";
}

TreeNode* deserialize(string s)
{
	assert(s.front() == '[' && s.back() == ']');
	size_t i = 1;//scape first `['
	vector<TreeNode*> nodes;
	while (true)
	{
		while (s[i] == ' ' || s[i] == ',')
			i++; // scape space & `,'
		if (s[i] == ']') break;
		if (s[i] == 'n')
		{
			nodes.push_back(nullptr);
			i += 4;
		}
		else
		{
			nodes.push_back(new TreeNode(atoi(s.c_str() + i)));
			while (isdigit(s[++i]));
		}
	}

	i = 1;
	size_t len = nodes.size();
	for (auto node : nodes)
	{
		if (node)
		{
			if (i == len) break;
			node->left = nodes[i++];
			if (i == len) break;
			node->right = nodes[i++];
		}
	}

	return len > 0 ? nodes[0] : nullptr;
}

string serialize(TreeNode* node)
{
	deque<TreeNode*> q{ node };
	vector<TreeNode*> result;

	while (!q.empty())
	{
		TreeNode* n = q.front();
		q.pop_front();
		result.push_back(n);
		if (n)
		{
			q.push_back(n->left);
			q.push_back(n->right);
		}
	}

	int tail = result.size() - 1;
	for (; tail >= 0; tail--)
		if (result[tail]) break;

	ostringstream out;
	out << '[';
	if (tail > 0)
		if (result[0])
			out << result[0]->val;
		else
			out << "null";
	for (int i = 1; i <= tail; i++)
	{
		out << ", ";
		if (result[i])
			out << result[i]->val;
		else
			out << "null";
	}
	out << ']';
	return out.str();
}