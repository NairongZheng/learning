
"""
    删除排序链表中的重复元素
    给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        slow = fast = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None        # 要断开后面重复的元素
        return head
