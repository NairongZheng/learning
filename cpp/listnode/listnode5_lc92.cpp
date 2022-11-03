/*
    反转链表II
    给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
    请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
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
    ListNode *reverseList(ListNode *head)
    {
        if (head == NULL)
        {
            return NULL;
        }
        ListNode *temp;
        ListNode *pre = NULL;
        ListNode *cur = head;
        while (cur)
        {
            temp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = temp;
        }
        return pre;
    }

    ListNode *reverseBetween(ListNode *head, int left, int right)
    {
        ListNode *dummy = new ListNode(0, head);
        ListNode *pre = dummy;

        // 第一步：走到left节点的前一个节点
        for (int i = 0; i < left - 1; i++)
        {
            pre = pre->next;
        }

        // 第二步：来到right节点
        ListNode *right_node = pre;
        for (int i = 0; i < right - left + 1; i++)
        {
            right_node = right_node->next;
        }

        // 第三步：切割出一个子链表
        ListNode *left_node = pre->next;
        ListNode *post = right_node->next;
        pre->next = NULL;
        right_node->next = NULL;

        // 第四步：翻转链表
        reverseList(left_node);

        // 第五步：接回原来的链表中
        pre->next = right_node;
        left_node->next = post;
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
    // 构建链表
    ListNode *node1 = new ListNode(1);
    ListNode *node2 = new ListNode(2);
    ListNode *node3 = new ListNode(3);
    ListNode *node4 = new ListNode(4);
    ListNode *node5 = new ListNode(5);
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;

    int left = 2;
    int right = 4;
    Solution *obj = new Solution();
    ListNode *reverse_head = obj->reverseBetween(node1, left, right);
    printListNode(reverse_head); // 1 4 3 2 5
    return 0;
}