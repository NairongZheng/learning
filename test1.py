# Definition for a binary tree node.
from stack_queue.stack_queue7_lc239_star import Solution


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
        result = []
        if not root:
            return ''
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node != '#':
                result.append(str(node.val))
                if node.left:
                    stack.append(node.left)
                else:
                    stack.append('#')
                if node.right:
                    stack.append(node.right)
                else:
                    stack.append('#')
            else:
                result.append('#')
        print(result)
        return ''.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        def construct_tree(nums, index):
            if index >= len(nums):
                return
            if nums[index] == '#':
                return None
            left = index * 2 + 1
            right = index * 2 + 2
            root = TreeNode(int(nums[index]))
            root.left = construct_tree(nums, left)
            root.right = construct_tree(nums, right)
            return root
        root = construct_tree(data, 0)
        return root

aaa = Codec()
bbb = aaa.deserialize("123##4567####")
pass

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))