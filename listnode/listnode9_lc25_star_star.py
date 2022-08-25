"""
    k个一组反转链表

    顺便把反转链表，反转部分链表总结一下
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        """
            反转以head为头节点的链表
        """
        if not head:
            return None
        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
    def reverseBetween(self, headA, headB):
        """
            （这个只是个示例帮助理解）
            反转headA和headB之间的元素，注意是左闭右开
            反转以head为头节点的链表其实就是反转head到None之间的节点
            那么反转headA到headB之间的节点，只要把终止条件改了就行
        """
        cur = headA
        pre = None
        while cur != headB:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
    def reverseKGroup(self, head, k):
        """
            k个一组反转链表
        """
        if not head:
            return None
        headA = headB = head
        for i in range(k):
            if not headB:       # 不足k个，不用反转
                return head
            headB = headB.next
        newHead = self.reverseBetween(headA, headB)     # 反转前k个元素
        headA.next = self.reverseKGroup(headB, k)       # 递归反转后序链表并连接起来
        return newHead
    
    def print(self, head):
        """
            打印看看
        """
        result = []
        if not head:
            print(result)
            return
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        print(result)
        return
    
    def build_listnode(self):
        node1, node2, node3 = ListNode(1), ListNode(2), ListNode(3)
        node4, node5 = ListNode(4), ListNode(5)
        node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
        return node1

aaa = Solution()

# 打印链表
node1 = aaa.build_listnode()
aaa.print(node1)        # [1, 2, 3, 4, 5]

# 反转链表
node1 = aaa.build_listnode()
reverseList_head = aaa.reverseList(node1)
aaa.print(reverseList_head)     # [5, 4, 3, 2, 1]

# 反转a到b之间（其实不是）
node1, node2, node3 = ListNode(1), ListNode(2), ListNode(3)
node4, node5 = ListNode(4), ListNode(5)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
reverseBetween_head = aaa.reverseBetween(node1, node3)
aaa.print(reverseBetween_head)      # [2, 1]

# k个一组反转
node1 = aaa.build_listnode()
reverseKGroup_head = aaa.reverseKGroup(node1, 2)
aaa.print(reverseKGroup_head)      # [2, 1, 4, 3, 5]

