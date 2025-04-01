
"""
题目链接：https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val):
        """
            给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 
            输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
        """
        # # 递归法-无返回值
        # if not root:
        #     return TreeNode(val)
        # if not root.left and val < root.val:
        #     root.left = TreeNode(val)
        # if not root.right and val > root.val:
        #     root.right = TreeNode(val)
        
        # if val < root.val:
        #     self.insertIntoBST(root.left, val)
        # if val > root.val:
        #     self.insertIntoBST(root.right, val)
        # return root


        # 递归法-有返回值
        if not root:        # 递归终止条件：遇到空节点，这就是要插入的位置
            return TreeNode(val)

        # 单层递归逻辑
        if val < root.val:
            # 将val插入至当前root的左子树中合适的位置
            # 并更新当前root的左子树为包含目标val的新左子树
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root


        # # 迭代法-与无返回值的递归函数的思路大体一致
        # if not root:
        #     return TreeNode(val)
        
        # parent = None
        # cur = root

        # # 用while循环不断找新节点的parent
        # while cur:
        #     if val > cur.val:
        #         parent = cur
        #         cur = cur.right
        #     elif val < cur.val:
        #         parent = cur
        #         cur = cur.left
        
        # # 运行到这意味着已经跳出上面的while循环
        # # 同时意味着新节点的parent已经被找到
        # # parent已经被找到，新节点已经ready，把两个节点接在一起就可以了
        # if val > parent.val:
        #     parent.right = TreeNode(val)
        # if val < parent.val:
        #     parent.left = TreeNode(val)
        # return root


def main():
    # 构建一棵树
    from tree11_lc106_star import Solution as Solution_build
    from tree4_lc102 import Solution as Solution_print
    inorder = [1, 2, 3, 4, 7]
    postorder = [1, 3, 2, 7, 4]
    root = Solution_build().buildTree(inorder, postorder)
    result_root = Solution().insertIntoBST(root, 5)
    res_list = Solution_print().levelOrder(result_root)
    print(res_list) # [[4], [2, 7], [1, 3, 5]]


if __name__ == '__main__':
    main()