/*
    移除链表元素
    删除链表中所有满足Node.val == val的节点
    注意是所有，而不是第一个
*/

#include <iostream>
#include <vector>
using namespace std;

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *removeElements(ListNode *head, int val)
    {
        ListNode *dummy = new ListNode(0, head);
        ListNode *cur = dummy;
        while (cur && cur->next)
        {
            if (cur->next->val == val)
            {
                cur->next = cur->next->next;
            }
            else
            {
                cur = cur->next;
            }
        }
        return dummy->next;
    }
};

void printListNode(ListNode *head)
{
    if (head == NULL)
    {
        return;
    }
    while (head)
    {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

int main()
{
    ListNode *node1 = new ListNode(1);
    ListNode *node2 = new ListNode(2);
    ListNode *node3 = new ListNode(3);
    node1->next = node2;
    node2->next = node3;
    int val = 2;
    Solution *obj = new Solution();
    ListNode *reverse_head = obj->removeElements(node1, val);
    printListNode(reverse_head); // 1 3
    return 0;
}