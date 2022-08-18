"""
    填充每个节点的下一个右侧节点指针
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):

        if not root:
            return None

        # 思路一：遍历      # 这题没办法用思路二：分解问题来做
        def traverse(node1, node2):
            if not node1 or not node2:
                return
            # 前序位置
            node1.next = node2                  # 将传入的两个节点穿起来
            traverse(node1.left, node1.right)   # 连接相同父节点的两个子节点
            traverse(node2.left, node2.right)   # 连接相同父节点的两个子节点
            traverse(node1.right, node2.left)   # 连接跨越父节点的两个子节点
        
        traverse(root.left, root.right)
        return root

        # # 层序遍历
        # if not root:
        #     return None
        # stack = [root]
        # while stack:
        #     n = len(stack)
        #     for i in range(n):
        #         node = stack.pop(0)
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        #         if i == n - 1:        # 最后一个指向的是null
        #             break
        #         node.next = stack[0]
        # return root