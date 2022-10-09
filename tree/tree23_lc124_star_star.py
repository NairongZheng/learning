
# 不太好懂，但是可以类比tree18

"""
    二叉树中的最大路径和
    路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。
    该路径 至少包含一个 节点，且不一定经过根节点。
    路径和 是路径中各节点值的总和。
"""

import tree0

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = float('-inf')

    # 用分解问题的思路
    def maxPathSum(self, root):
        if not root:
            return 0
        self.one_side_max(root)
        return self.result
    
    # 定义：计算从根节点 root 为起点的最大单边路径和
    def one_side_max(self, root):
        if not root:
            return 0
        left_max_sum = max(0, self.one_side_max(root.left))
        right_max_sum = max(0, self.one_side_max(root.right))

        ###############################顺便做的，不是本来这个函数实现的功能###############
        path_max_sum = root.val + left_max_sum + right_max_sum      # 后序遍历位置，顺便更新最大路径和（左边最大+右边最大+本节点）
        self.result = max(self.result, path_max_sum)
        #################################################################################

        # 实现函数定义，左/右子树的最大单边路径和加上根节点的值，就是从根节点 root 为起点的最大单边路径和
        return max(left_max_sum, right_max_sum) + root.val


nums = [-10, 9, 20, 'null', 'null', 15, 7]
root = tree0.construct_binary_tree(nums, 0)

aaa = Solution()
bbb = aaa.maxPathSum(root)
print(bbb)          # 15+20+7=42

#           -10
#       9       20
#             15    7