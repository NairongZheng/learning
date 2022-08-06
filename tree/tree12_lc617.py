"""
    合并二叉树
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

# 1树如下
#        1
#    3       2
# 5
node11, node12, node13, node14 = TreeNode(1), TreeNode(3), TreeNode(2), TreeNode(5)
node11.left, node11.right = node12, node13
node12.left = node14

# 2树如下
#        2
#    1       3
#      4       7
node21, node22, node23, node24, node25 = TreeNode(2), TreeNode(1), TreeNode(3), TreeNode(4), TreeNode(7)
node21.left, node21.right = node22, node23
node22.right = node24
node23.right = node25

aaa = Solution()
bbb = aaa.mergeTrees(node11, node21)

# 合比树如下
#        3
#    4       5
#  5    4       7

# 用层序遍历检验一下
from tree4_lc102 import Solution as S
ccc = S()
ddd = ccc.levelOrder(bbb)
print(ddd)      # [[3], [4, 5], [5, 4, 7]]