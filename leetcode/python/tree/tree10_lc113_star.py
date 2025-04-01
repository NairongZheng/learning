"""
    二叉树路径总和II
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        """
            给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

            思路：要遍历整个树，找到所有路径，所以递归函数不要返回值！
        """
        # # 递归
        # path = []
        # result = []
        # def traversal(cur_node, remain):
        #     if not cur_node.left and not cur_node.right:
        #         if remain == 0:
        #             result.append(path[:])
        #         return
        #     if cur_node.left:
        #         path.append(cur_node.left.val)
        #         traversal(cur_node.left, remain - cur_node.left.val)
        #         path.pop()
        #     if cur_node.right:
        #         path.append(cur_node.right.val)
        #         traversal(cur_node.right, remain - cur_node.right.val)
        #         path.pop()
        # if not root:
        #     return []
        # path.append(root.val)
        # traversal(root, targetSum - root.val)
        # return result

        # 迭代-bfs
        if not root:
            return []
        stack = [root]
        temp = [(root.val, [root.val])]
        result = []
        while stack:
            for _ in range(len(stack)):
                node = stack.pop(0)
                value, path = temp.pop(0)
                if not node.left and not node.right:
                    if value == targetSum:
                        result.append(path)
                if node.left:
                    stack.append(node.left)
                    temp.append((node.left.val + value, path + [node.left.val]))
                if node.right:
                    stack.append(node.right)
                    temp.append((node.right.val + value, path + [node.right.val]))
        return result


def main():
    # 构建一棵树
    #       3
    #   9       2
    #         15    7
    node1, node2, node3 = TreeNode(3), TreeNode(9), TreeNode(2)
    node4, node5 = TreeNode(15), TreeNode(7)

    node1.left, node1.right = node2, node3
    node3.left, node3.right = node4, node5

    aaa = Solution()
    bbb = aaa.pathSum(node1, 12)
    print(bbb)          # [[3, 9], [3, 2, 7]]


if __name__ == '__main__':
    main()