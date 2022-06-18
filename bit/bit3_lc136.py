

def singleNumber(nums):
    """
        只出现一次的数字
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    """

    # 异或的性质：
    # 1. 任何数和0异或都是它本身
    # 2. 任何数和自己异或都是0
    result = 0
    for i in range(len(nums)):
        result = result ^ nums[i]
    return result

aaa = singleNumber([4,1,2,1,2])
print(aaa)