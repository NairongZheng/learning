# https://leetcode.cn/problems/linked-list-cycle/description

from typing import Optional
from utils.build_cycle_listnode import build_cycle_listnode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


def main():
    test_list = [
        [[3, 2, 0, -4], 1],  # true
        [[1, 2], 0],  # true
        [[1], -1],  # false
    ]
    for arr, pos in test_list:
        head = build_cycle_listnode(arr, pos)
        res = Solution().hasCycle(head)
        print(f"res: {res}")


if __name__ == "__main__":
    main()
