"""
    环形链表II
    给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:        # 快慢指针相遇说明有环，此时slow走过x+y，fast走过x+y+n(y+z)，所以有2(x+y)=x+y+n(y+z)，可以得到x=(n-1)(y+z)+z
                p = head
                q = slow
                while p != q:       # 也就是说，从(1)头节点，(2)相遇的点，一起走，再次相遇就是环的入口
                    p = p.next
                    q = q.next
                return q
        return None                 # 无环返回None