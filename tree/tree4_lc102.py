"""
    二叉树的层序遍历
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        # 层序遍历

        # 递归
        result = []
        def helper(root, depth):
            if not root:        # 递归结束条件
                return []
            if len(result) == depth:    # 新的一层用一个新数组保存当前层的值
                result.append([])
            result[depth].append(root.val)
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)
        helper(root, 0)
        return result

        # # 迭代
        # results = []
        # if not root:
        #     return results
        # stack = [root]
        # while stack:
        #     n = len(stack)
        #     result = []
        #     for _ in range(n):
        #         cur = stack.pop(0)
        #         result.append(cur.val)
        #         if cur.left:
        #             stack.append(cur.left)
        #         if cur.right:
        #             stack.append(cur.right)
        #     results.append(result)
        # return results

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
bbb = aaa.levelOrder(node1)
print(bbb)      # [[5], [4, 6], [1, 2, 7, 8]]