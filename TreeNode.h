#pragma once
#include <vector>

#ifndef TREE_NODE
#define TREE_NODE

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	explicit TreeNode(int x, TreeNode* _l = nullptr, TreeNode* _r = nullptr)
		:val(x), left(_l), right(_r) {}
};

#define tl(d,root,l) d[root].left = &d[l];
#define tr(d,root,r) d[root].right = &d[r];

std::vector<TreeNode> make_tree(size_t n)
{
	std::vector<TreeNode> res{ n, TreeNode{0} };
	for (size_t i = 0; i < n; i++)
	{
		res[i].val = i;
	}
	return res;
}

std::ostream& operator<< (std::ostream& os, TreeNode* node);

TreeNode* deserialize(std::string s);
std::string serialize(TreeNode* node);

#endif