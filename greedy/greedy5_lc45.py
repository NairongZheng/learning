

def jump(nums):
    """
        跳跃游戏II
        给定一个非负整数数组, 你最初位于数组的第一个位置
        数组中的每个元素代表你在该位置可以跳跃的最大长度
        你的目标是使用最少的跳跃次数到达数组的最后一个位置
        假设你总是可以到达数组的最后一个位置

        贪心的思路, 局部最优: 当前可移动距离尽可能多走, 如果还没到终点, 步数再加一. 整体最优: 一步尽可能多走, 从而达到最小步数
        所以要从覆盖范围出发, 不管怎么跳, 覆盖范围内一定是可以跳到的, 以最小的步数增加覆盖范围, 覆盖范围一旦覆盖了终点, 得到的就是最小步数
        这里需要统计两个覆盖范围, 当前这一步的最大覆盖和下一步最大覆盖
        如果移动下标达到了当前这一步的最大覆盖最远距离了, 还没有到终点的话, 那么就必须再走一步来增加覆盖范围, 直到覆盖范围覆盖了终点
    """
    if len(nums) == 1:
        return 0
    ans = 0                     # 记录走的最大步数
    curDistance = 0             # 记录当前覆盖最远距离的下标
    nextDistance = 0            # 下一步覆盖的最远距离下标
    for i in range(len(nums)):
        nextDistance = max(i + nums[i], nextDistance)       # 更新下一步覆盖的最远距离下标
        if i == curDistance:                                # 遇到当前覆盖的最远距离的下标
            if curDistance != len(nums) - 1:
                ans += 1
                curDistance = nextDistance                  # 更新当前覆盖的最远距离的下标
                if nextDistance >= len(nums) - 1:
                    break
    return ans

aaa = jump([2,3,1,1,4])
print(aaa)
