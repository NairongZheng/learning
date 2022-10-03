

def lowestCommonAncestor(root, p, q):
    """
        二叉树的最近公共祖先
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

        思路：
        遇到这个题目首先想的是要是能自底向上查找就好了，这样就可以找到公共祖先了。
        二叉树回溯的过程就是从低到上。后序遍历就是天然的回溯过程，最先处理的一定是叶子节点。
    """

    # 递归
    # 1. 确定递归函数返回值以及参数
    #       需要递归函数返回值，来告诉我们是否找到节点q或者p，那么返回值为bool类型就可以了。但我们还要返回最近公共节点
    # 2. 确定终止条件：如果找到了 节点p或者q，或者遇到空节点，就返回。
    # 3. 确定单层递归逻辑：!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!看看博客吧，注意看那个图好好理解
    #       值得注意的是 本题函数有返回值，是因为回溯的过程需要递归函数的返回值做判断，但本题我们依然要遍历树的所有节点。
    #       在递归函数有返回值的情况下：
    #       1. 如果要搜索一条边，递归函数返回值不为空的时候，立刻返回，
    #       2. 如果搜索整个树，直接用一个变量left、right接住返回值，这个left、right后序还有逻辑处理的需要，也就是后序遍历中处理中间节点的逻辑（也是回溯）。


    # 看这个思路https://www.cnblogs.com/labuladong/p/13976582.html
    
    # base case
    if not root or root == p or root == q:
        return root

    # 递归
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)


    if left and right:      # 情况一：如果left 和 right都不为空，说明此时root就是最近公共节点。
        return root
    if left is None and right is None:                # 情况二：都为None，返回None
        return left
    return left if left else right             # 情况三：哪个非空就返回哪个

    # # 情况二其实可以跟情况三合并（情况二删了也可以）：