"""
    二叉树的后序遍历
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        # 后续遍历(左右中)

        # # 递归
        # def traversal(root):
        #     if not root:
        #         return
        #     traversal(root.left)      # 左
        #     traversal(root.right)     # 右
        #     result.append(root.val)   # 中
        # result = []
        # traversal(root)
        # return result

        # 迭代
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur)               # 中
                stack.append(None)
                if cur.right:
                    stack.append(cur.right)     # 右
                if cur.left:
                    stack.append(cur.left)      # 左
            else:
                cur = stack.pop()
                result.append(cur.val)
        return result


def main():
    # 构建一棵树
    #       5
    #   4       6
    # 1   2   7   8
    node1, node2, node3, node4 = TreeNode(5), TreeNode(4), TreeNode(6), TreeNode(1)
    node5, node6, node7 = TreeNode(2), TreeNode(7), TreeNode(8)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7

    aaa = Solution()
    bbb = aaa.postorderTraversal(node1)
    print(bbb)      # [1, 2, 4, 7, 8, 6, 5]


if __name__ == '__main__':
    main()