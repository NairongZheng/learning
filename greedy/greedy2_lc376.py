
def wiggleMaxLength(nums):
    """
        摆动序列
        如果连续数字之间的差严格地在正数和负数之间交替, 则数字序列称为摆动序列
        第一个差(如果存在的话)可能是正数或负数. 少于两个元素的序列也是摆动序列
        给定一个整数序列, 返回作为摆动序列的最长子序列的长度
        通过从原始序列中删除一些(也可以不删除)元素来获得子序列, 剩下的元素保持其原始顺序
    """
    preC = 0        # 上一个差值
    curC = 0        # 当前差值
    result = 1
    for i in range(len(nums) - 1):
        curC = nums[i + 1] - nums[i]
        if curC * preC <= 0 and curC != 0:  # 差值为0时, 不算摆动
            result += 1
            preC = curC     # 如果当前差值和上一个差值为一正一负时, 才需要用当前差值替代上一个差值
    return result

aaa = wiggleMaxLength([1,7,4,9,2,5])
print(aaa)