"""
    二叉树的前序遍历
    (中左右)
"""

# Definition for a binary tree node.
from unittest import result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def preorderTraversal(self, root):

        # 递归法(思路二：分解问题)
        # 一棵二叉树的前序遍历结果 = 根节点 + 左子树的前序遍历结果 + 右子树的前序遍历结果。
        # 见参考链接

        # 递归法(思路一：遍历)
        result = []
        def traversal(root):
            if not root:    # 递归结束条件：遇到空节点就返回
                return
            result.append(root.val)     # 中
            traversal(root.left)        # 左
            traversal(root.right)       # 右
        traversal(root)
        return result

        # # 迭代法
        # result = []
        # if not root:
        #     return result
        # stack = [root]
        # while stack:
        #     cur = stack.pop()
        #     if cur:
        #         if cur.right:
        #             stack.append(cur.right)       # 右
        #         if cur.left:
        #             stack.append(cur.left)        # 左
        #         stack.append(cur)                 # 中
        #         stack.append(None)
        #     else:
        #         cur = stack.pop()
        #         result.append(cur.val)
        # return result

# 构建一棵树
#       5
#   4       6
# 1   2   7   8
node1, node2, node3, node4 = TreeNode(5), TreeNode(4), TreeNode(6), TreeNode(1)
node5, node6, node7 = TreeNode(2), TreeNode(7), TreeNode(8)

node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.left, node3.right = node6, node7

aaa = Solution()
bbb = aaa.preorderTraversal(node1)
print(bbb)      # [5, 4, 1, 2, 6, 7, 8]