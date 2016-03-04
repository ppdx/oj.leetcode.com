#pragma once
#include <iosfwd>
#ifndef LIST_NODE_H
#define LIST_NODE_H

struct ListNode
{
	int val;
	ListNode *next;
	explicit ListNode(int x, ListNode* _next = nullptr) : val(x), next(_next) {}
};

template<typename iter>
ListNode* make_linkedlist(iter begin, iter end)
{
	ListNode* head = nullptr;
	if (begin != end)
	{
		head = new ListNode(*begin);
		++begin;
	}

	ListNode* p = head;
	while (begin != end)
	{
		p->next = new ListNode(*begin);
		p = p->next;
		++begin;
	}
	return head;
}

void delete_linkedlist(ListNode* head);

std::ostream& operator<<(std::ostream& os, ListNode* head);

#endif // !LIST_NODE_H
