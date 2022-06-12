

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add_element(self, node_value):
        node = Node(node_value)
        if self.root is None:       # 如果root不存在, 就直接挂上去
            self.root = node
            return

        # 如果root存在, 就要去搜索应该挂在这个树的哪里, 就要用到BFS
        queue = [self.root]
        while True:
            pop_node = queue.pop(0)

            if pop_node.left is None:
                pop_node.left = node
                return
            else:
                queue.append(pop_node.left)

            if pop_node.right is None:
                pop_node.right = node
                return
            else:
                queue.append(pop_node.right)

    def dfs_preorder(self, root):
        """
            前序遍历
        """
        if root is None:
            return
        print(root.val, end=' ')
        self.dfs_preorder(root.left)
        self.dfs_preorder(root.right)

    def dfs_inorder(self, root):
        """
            中序遍历
        """
        if root is None:
            return
        self.dfs_inorder(root.left)
        print(root.val, end=' ')
        self.dfs_inorder(root.right)

    def dfs_postorder(self, root):
        """
            后续遍历
        """
        if root is None:
            return
        self.dfs_postorder(root.left)
        self.dfs_postorder(root.right)
        print(root.val, end=' ')

tree = Tree()
tree.add_element(1)
tree.add_element(2)
tree.add_element(3)
tree.add_element(4)
tree.add_element(5)
tree.add_element(6)
tree.add_element(7)
tree.dfs_preorder(tree.root)    # 1245367
tree.dfs_inorder(tree.root)     # 4251637
tree.dfs_postorder(tree.root)   # 4526731

"""
      1
   2     3
  4 5   6 7
"""
