
# 恰好
# 这题在leetcode是hard难度, 一般滑动窗口hard难度都是跟前缀和结合的
def subarraysWithKDistinct(nums, k):
    """
        K个不同整数的子数组:
        给定一个正整数数组nums和一个整数k, 返回num中'好子数组'的数目。
        如果nums的某个子数组中不同整数的个数恰好为k, 则称nums的这个连续、不一定不同的子数组为'好子数组'
        例如, [1,2,3,1,2] 中有 3个不同的整数:1,2,以及3。
        子数组是数组的连续部分。

        恰好为k!!!!!!!!  904题就是小于等于, 而这题是等于. 只取等于的话就比较复杂
        其实等于就要涉及滑动窗口回缩, 但是可以用<=k 的结果减去 <=(k-1)的结果, 就是刚好等于k了
    """

    def leK(nums, k):
        """
            找小于等于k的函数
        """
        start = 0
        adict = {}
        count = 0
        for end in range(len(nums)):
            if nums[end] not in adict:
                adict[nums[end]] = 1
            else:
                adict[nums[end]] += 1
            
            while len(adict) > k:       # 因为要找小于等于k的, 所以当大于k的时候就要改变窗口了
                adict[nums[start]] -= 1
                if adict[nums[start]] == 0:
                    del adict[nums[start]]
                start += 1

            # 现在问题来了, 我们卡出了一个符合要求的窗口, 那这个窗口里面有几个不同的子数组呢???????????
            count += (end - start + 1)
            # 为什么是end-start+1, 假设nums=[1,2,3,1,2], 现在卡出来的窗口是[1,2,3], 
            # 那么符合要求的子数组有[1],[2],[1,2]
            # 那不是有三个吗? 而end-start+1==2
            # 所以其实统计的只有[2],[1,2], 因为有一个是在前面统计的
            # (还是看视频去吧)
        return count
    return leK(nums, k) - leK(nums, k - 1)

aaa = subarraysWithKDistinct([1,2,1,2,3], 2)
print(aaa)
