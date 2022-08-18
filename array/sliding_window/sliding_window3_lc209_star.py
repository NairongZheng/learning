

# 不定长的滑动窗口
def minSubArrarLen(s, nums):
    """
        长度最小的子数组
        描述: 找出该数组中满足其和>=target的长度最小的连续子数组[numsl, numsl+1, ..., numsr-1, numsr],
        并返回其长度. 如果不存在符合条件的子数组, 返回0
    """
    start = 0
    cur_sum = 0
    min_len = float('inf')
    for end in range(len(nums)):
        cur_sum += nums[end]
        while cur_sum >= s:             # 有的题用if, 这边为什么用while, 想想就知道了其实
            min_len = min(min_len, end - start + 1)     # 窗口长度end-start+1
            cur_sum -= nums[start]      # 这步跟下一步就是用来移动窗口的, 窗口改变, 相应的值也要减去
            start += 1                  # 移动窗口, 只要移动了窗口, cur_sum就要变, 就是说要有上一步
        # 出了while循环, 说明cur_sum < s, 这个时候就继续进行for循环移动end把窗口变大就可以了
    
    if min_len == float('inf'):         # 如果根本没变化就说明找遍了都不符合条件, 根据要求返回0
        return 0
    else:
        return min_len

aaa = minSubArrarLen(s=7, nums=[2,3,1,2,4,3])
print(aaa)