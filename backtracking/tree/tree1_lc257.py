

def binaryTreePaths(root):
    """
        二叉树的所有路径
        给定一个二叉树，返回所有从根节点到叶子节点的路径。

        思路:
        这道题目要求从根节点到叶子的路径，所以需要前序遍历，这样才方便让父节点指向孩子节点，找到对应的路径。
        在这道题目中将第一次涉及到回溯，因为我们要把路径记录下来，需要回溯来回退一一个路径在进入另一个路径。
        我们先使用递归的方式，来做前序遍历。要知道递归和回溯就是一家的，本题也需要回溯。
    """
    # # 递归法+隐形回溯
    # def traversal(cur, path, result):
    #     path += str(cur.val)
    #     if not cur.left and not cur.right:
    #         result.append(path)
    #     if cur.left:
    #         # + '->' 是隐藏回溯
    #         traversal(cur.left, path + '->', result)
    #     if cur.right:
    #         traversal(cur.right, path + '->', result)

    # path = ''
    # result = []
    # if not root:
    #     return result
    # traversal(root, path, result)
    # return result

    # 迭代法(bfs)
    stack = [root]
    path_stack = []
    result = []
    path_stack.append(str(root.val))
    while stack:
        cur = stack.pop()
        path = path_stack.pop()
        # 如果当前节点为叶子节点，添加路径到结果中
        if not (cur.left or cur.right):
            result.append(path)
        if cur.right:
            stack.append(cur.right)
            path_stack.append(path + '->' + str(cur.right.val))
        if cur.left:
            stack.append(cur.left)
            path_stack.append(path + '->' + str(cur.left.val))
    return result