class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = root.right
            while node.left:
                node = node.right
            node.left = root.left
            root = root.right
        return root