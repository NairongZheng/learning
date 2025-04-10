

# 子集问题
def findSubsequences(nums):
    """
        递增子序列
        给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
        数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

        思路：
        本题求自增子序列，是不能对原数组进行排序的，排完序的数组都是自增子序列了。
        所以不能使用之前的去重逻辑！！！！

       这边的usage_list不同之前，这也是需要注意的点
       usage_list是记录本层元素是否重复使用，新的一层usage_list都会重新定义（清空），所以要知道usage_list只负责本层！（不是很明白）
    """
    path = []
    result = []
    def backtracking(startIndex):
        if len(path) >= 2:
            result.append(path[:])
        if startIndex == len(nums):
            return
        usage_list = set()      # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        for i in range(startIndex, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in usage_list:
                continue
            usage_list.add(nums[i])
            path.append(nums[i])
            backtracking(i + 1)
            path.pop()
    backtracking(0)
    return result

aaa = findSubsequences([4,6,7,7])
print(aaa)          # [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]