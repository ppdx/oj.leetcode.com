class Solution {
    int get_length(ListNode* head)
    {
        int length = 0;
        while (head)
        {
            length++;
            head = head->next;
        }
        return length;
    }
public:
    bool isPalindrome(ListNode* head) {
        int length = get_length(head);
        if (length <= 1) return true;
        int helf = length / 2 - 1;
        ListNode* right = head->next;
        auto left = head;
        left->next = nullptr;
        while (helf)
        {
            auto q = right->next;
            right->next = left;
            left = right;
            right = q;
            helf--;
        }
        if (length % 2 == 1) right = right->next;
        while (left)
        {
            if (left->val != right->val)
                return false;
            left = left->next;
            right = right->next;
        }
        return true;
    }
};
