"""
    二叉树的最小深度
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root):
        
        # 递归(不是很懂)
        def get_depth(node):
            if not node:        # 递归终止条件：空节点，表示高度为0
                return 0
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            if node.left is None and node.right is not None:
                return 1 + right_depth      # 如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度。
            if node.left is not None and node.right is None:
                return 1 + left_depth       # 如果右子树为空，左子树不为空，说明最小深度是 1 + 左子树的深度。 
            
            result = 1 + min(left_depth, right_depth)
            return result
        
        return get_depth(root)

        # # 迭代
        # if not root:
        #     return 0
        # stack = [root]
        # result = 1
        # while stack:
        #     for _ in range(len(stack)):
        #         node = stack.pop(0)
        #         if not node.left and not node.right:    # 左右节点都为空的时候找到了叶子节点
        #             return result
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        #     result += 1
        # return result

# 构建一棵树
#       1
#            2
#         4    3
#            6   5
node1, node2, node3 = TreeNode(1), TreeNode(2), TreeNode(4)
node4, node5, node6 = TreeNode(3), TreeNode(6), TreeNode(5)

node1.right = node2
node2.left, node2.right = node3, node4
node4.left, node4.right = node5, node6

aaa = Solution()
bbb = aaa.minDepth(node1)
print(bbb)          # 3