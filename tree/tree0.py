

# acm模式构建二叉树
# 注意：层序遍历，且，“完全二叉树”保存（没有的用null之类的表示）的，才可以用这个。
# 具体区别可以看看tree22

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree(nums, index):
    if index >= len(nums):
        return
    if nums[index] == 'null':     # 'null'的时候
        return None
    left = index * 2 + 1
    right = index * 2 + 2
    root = TreeNode(nums[index])
    root.left = construct_binary_tree(nums, left)
    root.right = construct_binary_tree(nums, right)
    return root


def preorderTraversal(root):        # 前序遍历
    result = []
    def traversal(root):
        if not root:    # 递归结束条件：遇到空节点就返回
            return
        result.append(root.val)     # 中
        traversal(root.left)        # 左
        traversal(root.right)       # 右
    traversal(root)
    return result

if __name__ == '__main__':
    nums = [3, 9, 20, 'null', 'null', 15, 7]
    print("输入数组为：", nums)                         # 输入数组为： [3, 9, 20, 'null', 'null', 15, 7]
    root = construct_binary_tree(nums, 0)
    print("二叉树已生成")
    print('中序遍历结果：', preorderTraversal(root))    # 中序遍历结果： [3, 9, 20, 15, 7]
