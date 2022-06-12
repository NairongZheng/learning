

def longestOnes(nums, k):
    """
        最大连续1的个数III: 
        给定一个二进制数组nums和一个整数k, 如果可以翻转最多k个0, 则返回数组中连续1的最大个数
    """
    max_len = float('-inf')
    start = 0
    count_one = 0
    for end in range(len(nums)):
        if nums[end] == 1:
            count_one += 1
        # count_one + k是极限长度, 就是最多只能有这么多1, 但是如果窗口长度(end-start+1)比这个极限长度还大, 
        # 就说明窗口是有问题的, 就需要改变窗口, 就是移动start
        while count_one + k < (end - start + 1):
            if nums[start] == 1:
                count_one -=1
            start += 1
        max_len = max(max_len, end - start + 1)

    if max_len == float('-inf'):
        return 0
    return max_len

aaa = longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print(aaa)