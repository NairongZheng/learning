
# 恰好
def numSubarrayWithSum(nums, goal):
    """
        和相同的二元子数组:找到和为goal的连续子数组的个数
        和为goal, 也是涉及回缩, 跟上一题等于k是一个道理
    """

    def leGoal(nums, goal):
        """
            返回的是和小于等于goal的子数组个数有多少
        """
        if goal < 0:
            return 0
        start = 0
        count_one = 0
        count = 0
        for end in range(len(nums)):
            if nums[end] == 1:
                count_one += 1
            while count_one > goal:
                if nums[start] == 1:
                    count_one -= 1
                start += 1
            # 在当前start和end满足要求框出来的滑动窗口可以相对于前面一个滑动窗口新增多少个和小于等于goal的子数组的个数
            # 假设上一个窗口是[1,0], 现在这个窗口是[1,0,1], 那么新增的3个就是[1,0,1],[0,1],[1]
            count += (end - start + 1)          # 只是恰好是窗口的长度, 只是恰好!！
        return count
    return leGoal(nums, goal) - leGoal(nums, goal - 1)

aaa = numSubarrayWithSum([1,0,1,0], 2)
print(aaa)