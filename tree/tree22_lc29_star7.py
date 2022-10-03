
"""
    二叉树的序列化与反序列化

    法一是不对的，用层序遍历的办法构造的话，依赖于是否是用“完全二叉树”的结构保存的。
    但是在序列化的时候法一没有按照“完全二叉树”，把空节点的左右都保存成空。所以是错的
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 法二
        result = []
        def helper(root, result):
            if root is None:
                result.append('#')
                result.append(',')          # 因为有可能是负数，或者百位十位，所以用","来把每个val隔开
                return
            result.append(str(root.val))    # 前序位置
            result.append(',')
            helper(root.left, result)
            helper(root.right, result)
        helper(root, result)
        return ''.join(result)


        # # 法一
        # result = []
        # if not root:
        #     return ''
        # stack = [root]
        # while stack:
        #     node = stack.pop(0)
        #     if node != '#':
        #         result.append(str(node.val))
        #         if node.left:
        #             stack.append(node.left)
        #         else:
        #             stack.append('#')
        #         if node.right:
        #             stack.append(node.right)
        #         else:
        #             stack.append('#')
        #     else:
        #         result.append('#')
        # print(result)
        # return ''.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 法二
        data = data.split(',')
        def helper(data):
            if len(data) == 0:
                return None
            root_val = data.pop(0)
            if root_val == '#':
                return None
            root = TreeNode(int(root_val))
            root.left = helper(data)
            root.right = helper(data)
            return root
        return helper(data)


        # # 法一
        # if len(data) == 0:
        #     return None
        # def construct_tree(nums, index):
        #     if index >= len(nums):
        #         return
        #     if nums[index] == '#':
        #         return None
        #     left = index * 2 + 1
        #     right = index * 2 + 2
        #     root = TreeNode(int(nums[index]))
        #     root.left = construct_tree(nums, left)
        #     root.right = construct_tree(nums, right)
        #     return root
        # root = construct_tree(data, 0)
        # return root