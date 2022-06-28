

def pathSum(root, targetSum):
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