# 顺便把tree23看了
"""
    二叉树的直径
    给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

    建议看看参考链接
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
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root):
        """
            解决这题的关键在于，每一条二叉树的「直径」长度，就是一个节点的左右子树的最大深度之和。
        """

        # 递归法(思路二：分解问题)(后序)
        def max_depth(root):
            if not root:
                return 0
            left_max = max_depth(root.left)
            right_max = max_depth(root.right)

            ###############################顺便做的，不是本来这个函数实现的功能###########################
            # 后序位置。后序位置可以接收到子树的返回值，就不用向下对每个节点又用一次递归函数去算它的深度了
            my_diameter = left_max + right_max
            self.max_diameter = max(self.max_diameter, my_diameter)     # 后序遍历位置顺便计算最大直径
            #############################################################################################

            return max(left_max, right_max) + 1
        max_depth(root)
        return self.max_diameter

        # # 递归法(思路一：遍历)(前序)
        # # 这个解法是正确的，但是运行时间很长，原因也很明显，
        # # 前序位置无法获取子树信息，所以只能让每个节点调用 max_depth 函数去算子树的深度。
        # # 那如何优化？我们应该把计算「直径」的逻辑放在后序位置，准确说应该是放在 max_depth 的后序位置，因为 max_depth 的后序位置是知道左右子树的最大深度的。
        # def max_depth(root):
        #     if not root:
        #         return 0
        #     left_max = max_depth(root.left)
        #     right_max = max_depth(root.right)
        #     return 1 + max(left_max, right_max)

        # def traverse(root):
        #     # 前序位置
        #     if not root:
        #         return 
        #     left_max = max_depth(root.left)       # 先算左子树最大深度
        #     right_max = max_depth(root.right)     # 再算右子树最大深度
        #     my_diameter = left_max + right_max    # 得到该节点最大直径
        #     self.max_diameter = max(self.max_diameter, my_diameter)   # 然后一直取最大
        #     # 但是在前序位置没办法获取子树的信息。只好写一个max_depth去计算左右子树的信息
        #     traverse(root.left)
        #     traverse(root.right)

        # traverse(root)
        # return self.max_diameter


nums = [1, 2, 3, 4, 5, 'null', 'null']
root = tree0.construct_binary_tree(nums, 0)

aaa = Solution()
bbb = aaa.diameterOfBinaryTree(root)
print(bbb)          # 3 ([4,2,1,3]或者[5,2,1,3])

#           1
#       2       3
#    4    5