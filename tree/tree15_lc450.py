"""
    删除二叉搜索树中的节点
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key):
        if not root:        # 第一种情况：没找到删除的节点，遍历到空节点直接返回了
            return None
        if root.val == key:         # 找到删除的节点
            if not root.left and not root.right:    # 第二种情况：左右孩子都空，返回None
                return None
            if not root.left:       # 第三种情况：左孩子为空，右孩子不为空，右孩子补位
                return root.right
            if not root.right:      # 第四种情况：右孩子为空，左孩子不为空，左孩子补位
                return root.left
            node = root.right       # #第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置
            while node.left:
                node = node.left
            node.left = root.left
            root = root.right
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root