#include "stdafx.h"

//template<typename iter>
//ListNode* make_linkedlist(iter begin, iter end)
//{
//	ListNode* head = nullptr;
//	if (begin != end)
//	{
//		head = new ListNode(*begin);
//		++begin;
//	}
//
//	ListNode* p = head;
//	while (begin != end)
//	{
//		p->next = new ListNode(*begin);
//		p = p->next;
//		++begin;
//	}
//	return head;
//}

void delete_linkedlist(ListNode* head)
{
	for (auto next = head->next; head; head = next, next = head->next)
	{
		delete head;
	}
}

std::ostream& operator<<(std::ostream& os, ListNode* head)
{
	if (head)
	{
		os << head->val;
		head = head->next;
	}

	while (head)
	{
		os << " -> ";
		os << head->val;
		head = head->next;
	}
	return os;
}
