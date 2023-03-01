
# 可以看stack_queue7

def maxSlidingWindow(nums, k):
    """
        滑动窗口的最大值
        给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
        你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

        思路：
        要找最大值，所以用一个最大堆来找
        因为固定窗口，所以要判断当前这个堆的最大值是不是在窗口里的，所以要记录下标
        如果不在窗口里，那这个最大值就不能用，就一直弹出
        直到最大堆的最大的那个值在窗口中，才添加到结果中
    """

    import heapq
    result = []
    maxheap = []

    # 先把前k个添加到最大堆中，并且在result中加入第一个窗口的最大值
    for i in range(k):
        heapq.heappush(maxheap, (-nums[i], i))
    result.append(-maxheap[0][0])

    for i in range(k, len(nums)):
        heapq.heappush(maxheap, (-nums[i], i))
        while maxheap[0][1] <= i - k:       # 如果这个堆中的最大值已经不在这个窗口里了，那么就一直弹出!!!!!这里是关键
            heapq.heappop(maxheap)
        result.append(-maxheap[0][0])
    return result


aaa = maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(aaa)