"""
    二叉树的中序遍历
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        # 中序遍历(左中右)

        # 递归
        result = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)        # 左
            result.append(root.val)     # 中
            traversal(root.right)       # 右
        traversal(root)
        return result

        # # 迭代
        # result = []
        # if not root:
        #     return result
        # stack = [root]
        # while stack:
        #     cur = stack.pop()
        #     if cur is not None:
        #         if cur.right:
        #             stack.append(cur.right)     # 右
        #         stack.append(cur)               # 中
        #         stack.append(None)
        #         if cur.left:
        #             stack.append(cur.left)      # 左
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
bbb = aaa.inorderTraversal(node1)
print(bbb)      # [1, 4, 2, 5, 7, 6, 8]