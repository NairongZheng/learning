
"""
    合并K个升序链表
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        import heapq
        if len(lists) == 0:
            return None
        dummy = ListNode(0)
        cur = dummy
        smallheap = []
        for head in lists:
            while head:
                heapq.heappush(smallheap, head.val)
                head = head.next
        while smallheap:
            node_val= heapq.heappop(smallheap)
            node = ListNode(node_val)
            cur.next = node
            cur = cur.next
        return dummy.next

        # # 数组排序的方法
        # if len(lists) == 0:
        #     return None
        # dummy = ListNode(0)
        # cur = dummy
        # all_val = []
        # for head in lists:
        #     while head:
        #         all_val.append(head.val)
        #         head = head.next
        # all_val.sort()
        # for val in all_val:
        #     node = ListNode(val)
        #     cur.next = node
        #     cur = cur.next
        # return dummy.next