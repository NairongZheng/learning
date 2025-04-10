

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root):
        """
            打家劫舍III
            在上次打劫完一条街道之后和一圈房屋后, 小偷又发现了一个新的可行窃的地区. 这个地区只有一个入口. 我们称之为"根". 
            除了"根"之外, 每栋房子有且只有一个"父"房子与之相连. 一番侦察之后, 聪明的小偷意识到这个地方的所有房屋的排列类似于一棵二叉树. 
            如果两个直接相连的房子在同一天晚上被打劫, 房屋将自动报警
        """
        result = self.rob_tree(root)
        return max(result[0], result[1])
    
    def rob_tree(self, node):
        """
            使用一个长度为2的数组, 记录当前节点偷与不偷所得到的的最大金钱. 所以本题dp数组就是一个长度为2的数组
            所以dp数组以及下标的含义: 下标为0记录不偷该节点所得到的的最大金钱, 下标为1记录偷该节点所得到的的最大金钱
        """
        if node is None:
            return (0, 0)
        left = self.rob_tree(node.left)                         # 通过递归左节点, 得到左节点偷与不偷的金钱
        right = self.rob_tree(node.right)                       # 通过递归右节点, 得到右节点偷与不偷的金钱
        val1 = node.val + left[1] + right[1]                    # 偷当前节点, 不能偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1])  # 不偷当前节点, 可偷可不偷子节点
        return (val1, val2)