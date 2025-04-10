"""
    平衡二叉树

    二叉树节点的深度：指从根节点到该节点的最长简单路径边的条数。
    二叉树节点的高度：指从该节点到叶子节点的最长简单路径边的条数。

    求深度可以从上到下去查 所以需要前序遍历（中左右）
    高度只能从下到上去查，所以只能后序遍历（左右中）
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):

        # 递归(本题不建议用迭代)
        def get_height(root):
            # 1.参数：当前传入节点；返回值：以当前传入节点为根节点的树的高度
            if not root:    # 2.终止条件：遇到空节点返回0
                return 0
            # 3.单层递归逻辑：
            # 分别求出其左右子树的高度，然后如果差值小于等于1，则返回当前二叉树的高度，否则则返回-1，表示已经不是二叉平衡树了。
            left_height = get_height(root.left)
            if left_height == -1:
                return -1
            right_height = get_height(root.right)
            if right_height == -1:
                return -1
            
            # 后序位置
            if abs(left_height - right_height) > 1:
                result = -1
            else:
                result = 1 + max(left_height, right_height)
            return result
        if get_height(root) == -1:
            return False
        else:
            return True


def main():
    # 构建一棵树
    #       3
    #   9       20
    #         15    7
    node1, node2, node3 = TreeNode(3), TreeNode(9), TreeNode(20)
    node4, node5 = TreeNode(15), TreeNode(7)

    node1.left, node1.right = node2, node3
    node3.left, node3.right = node4, node5

    aaa = Solution()
    bbb = aaa.isBalanced(node1)
    print(bbb)          # True


if __name__ == '__main__':
    main()