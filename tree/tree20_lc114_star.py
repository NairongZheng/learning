
"""
    二叉树展开为链表
    给你二叉树的根结点 root ，请你将它展开为一个单链表：
    展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
    展开后的单链表应该与二叉树 先序遍历 顺序相同。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # 因为要原地拉平，所以不能用迭代做到，用分解问题的思路
    # flatten定义：输入节点 root，然后 root 为根的二叉树就会被拉平为一条链表
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        # 有了这个函数定义，于一个节点 x，可以执行以下流程：
        # 1. 先利用 flatten(x.left) 和 flatten(x.right) 将 x 的左右子树拉平。
        # 2. 将 x 的右子树接到左子树下方，然后将整个左子树作为右子树。
        # 这样，以 x 为根的整棵二叉树就被拉平了，恰好完成了 flatten(x) 的定义。
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历位置(去看看参考链接的图)

        # 左右子树已经被拉平成一条链表
        left = root.left
        right = root.right

        # 将左子树作为右子树
        root.left = None
        root.right = left

        # 将原先右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right