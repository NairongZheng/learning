"""
    从中序与后序遍历序列构造二叉树

    相同思路题目：从前序与中序遍历序列构造二叉树(105)、最大二叉树(654)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        # 20220321抄
        
        # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
        if not postorder: 
            return None

        # 第二步: 后序遍历的最后一个就是当前的中间节点. 
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步: 找切割点. 
        separator_idx = inorder.index(root_val)

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边. 
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
        # 重点1: 中序数组大小一定跟后序数组大小是相同的. 
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]

        # 第六步: 递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

# 树如下
#       3
#   9       20
#         15    7
node1, node2, node3 = TreeNode(3), TreeNode(9), TreeNode(20)
node4, node5 = TreeNode(15), TreeNode(7)

node1.left, node1.right = node2, node3
node3.left, node3.right = node4, node5

aaa = Solution()
bbb = aaa.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])

# bbb就是构建好啦，为了检验对不对，用前序遍历打印出来看看
from tree1_lc144 import Solution as S
ccc = S()
ddd = ccc.preorderTraversal(bbb)
print(ddd)      # [3, 9, 20, 15, 7]