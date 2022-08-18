"""
    二叉树的最大深度
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
            self.depth = 0
            self.result = 0

    def traverse(self, root):
        if not root:
            return None
        # 前序位置
        self.depth += 1
        if not root.left and not root.right:
            self.result = max(self.result, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)
        self.depth -= 1
    
    # 定义：输入根节点，返回这棵二叉树的最大深度！！！！！！！！！！多读几遍
    def maxDepth(self, root):
        # # (1)递归法(思路一：遍历)
        # # 这个解法应该很好理解，但为什么需要在前序位置增加 depth，在后序位置减小 depth？
        # # 因为前面说了，前序位置是进入一个节点的时候，后序位置是离开一个节点的时候，depth 记录当前递归到的节点深度，你把 traverse 理解成在二叉树上游走的一个指针，所以当然要这样维护。
        # # 至于对 res 的更新，你放到前中后序位置都可以，只要保证在进入节点之后，离开节点之前（即 depth 自增之后，自减之前）就行了。
        # self.traverse(root)
        # return self.result

        # (2)递归法(思路二：分解问题)XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        if not root:
            return 0
        
        # 利用定义，计算左右子树的最大深度
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)

        # 后序位置
        # 整棵树的最大深度等于左右子树的最大深度取最大值，在加上根节点自己
        # 问题来了，为什么主要的代码逻辑集中在后序位置？
        # 因为这个思路正确的核心在于，你确实可以通过子树的最大深度推导出原树的深度，
        # 所以当然要首先利用递归函数的定义算出左右子树的最大深度，然后推出原树的最大深度，主要逻辑自然放在后序位置。
        result = max(left_max, right_max) + 1
        return result

        # # (3)迭代法
        # depth = 0
        # if not root:
        #     return depth
        # stack = [root]
        # while stack:
        #     n = len(stack)
        #     for _ in range(n):
        #         cur = stack.pop(0)
        #         if cur.left:
        #             stack.append(cur.left)
        #         if cur.right:
        #             stack.append(cur.right)
        #     depth += 1
        # return depth