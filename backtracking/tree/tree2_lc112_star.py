

def hasPathSum(root, targetSum):
    """
        路径总和
        给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

        可以采用递归也可以采用迭代
    """

    # 递归+回溯
    # 1.确定递归函数的参数和返回类型：
    #       参数：需要二叉树的根节点，还需要一个计数器，这个计数器用来计算二叉树的一条边之和是否正好是目标和，计数器为int型。
    #       递归函数什么时候需要返回值？什么时候不需要返回值？这里总结如下三点：
    #           如果需要搜索整棵二叉树且不用处理递归返回值，递归函数就不要返回值。（这种情况就是113.路径总和ii）
    #           如果需要搜索整棵二叉树且需要处理递归返回值，递归函数就需要返回值。 
    #           如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。（本题的情况）
    #       遍历的路线，并不要遍历整棵树，所以递归函数需要返回值，可以用bool类型表示。
    # def isornot(root, target_sum):
    #     if not root.left and not root.right and target_sum == 0:    # 遇到叶子节点，并且计数为0
    #         return True
    #     if not root.left and not root.right:                        # 遇到叶子节点，计数不为0
    #         return False
    #     if root.left:
    #         target_sum -= root.left.val
    #         if isornot(root.left, target_sum):
    #             return True
    #         target_sum += root.left.val
    #     if root.right:
    #         target_sum -= root.right.val
    #         if isornot(root.right, target_sum):
    #             return True
    #         target_sum += root.right.val
    #     return False
    
    # if not root:
    #     return False
    # else:
    #     return isornot(root, targetSum - root.val)
    

    # 迭代-层序遍历-bfs
    if not root:
        return False
    stack = []  # [(当前节点, 路径数值), ...]
    stack.append((root, root.val))
    while stack:
        cur_node, path_sum = stack.pop()
        if not cur_node.left and not cur_node.right and path_sum == targetSum:
            return True
        if cur_node.right:
            stack.append((cur_node.right, path_sum + cur_node.right.val))
        if cur_node.left:
            stack.append((cur_node.left, path_sum + cur_node.left.val))
    return False