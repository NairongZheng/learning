

def isValidBST(root):
    """
        给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

        思路：中序遍历完看看数组是不是严格递增就可以了，但是这样空间复杂度就高了
    """

    # 递归
    cur_max = float('-inf')
    def _isValidBST(root):
        nonlocal cur_max
        if not root:
            return True
        is_left_valid = _isValidBST(root.left)
        if cur_max < root.val:
            cur_max = root.val
        else:
            return False
        is_right_valid = _isValidBST(root.right)
        return is_left_valid and is_right_valid
    return _isValidBST(root)

    # 迭代省略