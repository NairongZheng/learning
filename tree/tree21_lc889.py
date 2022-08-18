"""
    根据前序和后序遍历构造二叉树
    给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。
    如果存在多个答案，您可以返回其中 任何 一个。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        # 通过前序中序，或者后序中序遍历结果可以确定唯一一棵原始二叉树，但是通过前序后序遍历结果无法确定唯一的原始二叉树。
        # 用后序遍历和前序遍历结果还原二叉树，解法逻辑上和通过前中构建或通过后中构建差不多，也是通过控制左右子树的索引来构建：
        # 1. 首先把前序遍历结果的第一个元素或者后序遍历结果的最后一个元素确定为根节点的值。
        # 2. 然后把前序遍历结果的第二个元素作为左子树的根节点的值。
        # 3. 在后序遍历结果中寻找左子树根节点的值，从而确定了左子树的索引边界，进而确定右子树的索引边界，递归构造左右子树即可。

        def build(preorder, pre_start, pre_end, postorder, post_start, post_end):
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])
            
            # 节点对应的值就是前序遍历数组的第一个元素
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # root.left 的值是前序遍历第二个元素
            # 通过前序和后序遍历构造二叉树的关键在于通过左子树的根节点
            # 确定 preorder 和 postorder 中左右子树的元素区间
            left_root_val = preorder[pre_start + 1]
            index = postorder.index(left_root_val)
            left_size = index - post_start + 1          # 左子树的元素个数
            
            # 递归构造左右子树
            root.left = build(preorder, pre_start + 1, pre_start + left_size, postorder, post_start, index)
            root.right = build(preorder, pre_start + left_size + 1, pre_end, postorder, index + 1, post_end - 1)
            return root
        
        return build(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)