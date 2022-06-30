
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    """
        给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 
        输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
    """
    # # 递归法-有返回值（省略有返回值的递归法）
    # # base case
    # if not root:
    #     return TreeNode(val)
    # # 单层递归逻辑
    # if val < root.val:
    #     # 将val插入至当前root的左子树中合适的位置
    #     # 并更新当前root的左子树为包含目标val的新左子树
    #     root.left = insertIntoBST(root.left, val)
    # if val > root.val:
    #     root.right = insertIntoBST(root.right, val)
    # return root

    # 迭代法-与无返回值的递归函数的思路大体一致
    if not root:
        return TreeNode(val)
    
    parent = None
    cur = root

    # 用while循环不断找新节点的parent
    while cur:
        if val > cur.val:
            parent = cur
            cur = cur.right
        elif val < cur.val:
            parent = cur
            cur = cur.left
    
    # 运行到这意味着已经跳出上面的while循环
    # 同时意味着新节点的parent已经被找到
    # parent已经被找到，新节点已经ready，把两个节点接在一起就可以了
    if val > parent.val:
        parent.right = TreeNode(val)
    if val < parent.val:
        parent.left = TreeNode(val)
    return root