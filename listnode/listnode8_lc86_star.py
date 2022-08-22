"""
    分隔链表
    给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
    你应当 保留 两个分区中每个节点的初始相对位置。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x):

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        small = dummy1
        big = dummy2
        cur = head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            
            tmp = cur.next      # 这边要注意把原来cur的next断开
            cur.next = None
            cur = tmp

        small.next = dummy2.next
        return dummy1.next

node1, node2, node3 = ListNode(1), ListNode(4), ListNode(3)
node4, node5, node6 = ListNode(2), ListNode(5), ListNode(2)
node1.next, node2.next, node3.next = node2, node3, node4
node4.next, node5.next = node5, node6

aaa = Solution()
bbb = aaa.partition(node1, 3)

result = []     # 测试一下
while bbb:
    result.append(bbb.val)
    bbb = bbb.next
print(result)       # [1, 2, 2, 4, 3, 5]