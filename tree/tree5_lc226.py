"""
    翻转二叉树

    这道题目使用前序遍历和后序遍历都可以，唯独中序遍历不方便，因为中序遍历会把某些节点的左右孩子翻转了两次！
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):

        # (思路二：分解问题)
        # 定义：将以 root 为根的这棵二叉树翻转，返回翻转后的二叉树的根节点!!!!!
        if not root:
            return None
        # 利用函数的定义，先翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # 然后交换左右子节点
        root.left = right
        root.right = left
        return root     # 和定义逻辑自恰：以 root 为根的这棵二叉树已经被翻转，返回 root

        # # 迭代法：广度优先（层序遍历）(思路一：遍历)
        # if not root:
        #     return root
        # queue = [root]
        # while queue:
        #     size = len(queue)
        #     for _ in range(size):
        #         node = queue.pop(0)
        #         node.left, node.right = node.right, node.left
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root

        # # 迭代法：深度优先（前序遍历）(思路一：遍历)
        # if not root:
        #     return root
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left   # 中
        #     if node.right:
        #         stack.append(node.right)                    # 右
        #     if node.left:
        #         stack.append(node.left)                     # 左
        # return root

        # # 递归：前序遍历(思路一：遍历)
        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root