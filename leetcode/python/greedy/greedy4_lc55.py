

def canJump(nums):
    """
        跳跃游戏
        给定一个非负整数数组, 你最初位于数组的第一个位置
        数组中的每个元素代表你在该位置可以跳跃的最大长度
        判断你是否能够到达最后一个位置

        思路: 贪心算法局部最优解: 每次取最大跳跃步数(取最大覆盖范围) 整体最优解: 最后得到整体最大覆盖范围, 看是否能到终点
        局部最优推出全局最优, 找不出反例, 试试贪心
        这道题目关键点在于: 不用拘泥于每次究竟跳跳几步, 而是看覆盖范围, 覆盖范围内一定是可以跳过来的, 不用管是怎么跳的
    """
    if len(nums) == 1:
        return True
    cover = 0
    i = 0
    while i <= cover:
        cover = max(cover, i + nums[i])
        if cover >= len(nums) - 1:
            return True
        i += 1
    return False

aaa = canJump([3,2,1,0,4])
print(aaa)      # False