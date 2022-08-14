
"""
    数据流的中位数
    设计一个支持以下两种操作的数据结构：
        void addNum(int num) - 从数据流中添加一个整数到数据结构中。
        double findMedian() - 返回目前所有元素的中位数。
    
    思路：
    (排序的方法会超时)
    利用两个堆来解题, 一个排序的数组nums分成两半,
    nums为偶数的时候中位数是左半边最大值和右半边最小值求和除以2
    nums为基数的时候是左半边的最大值
    所以左边建立一个大顶堆, 右边建立一个小顶堆, 保证左边的堆总是比右边的多一个数字！！！！！！
"""

# 好好看是可以理解的(两个堆的操作，有点像排序)
import heapq
class MedianFinder:

    def __init__(self):
        self.small_heap = []    # 小根堆，放右边的值
        self.big_heap = []      # 大根堆，放左边的值
        self.count = 0

    def addNum(self, num: int):
        self.count += 1
        # 为什么要让num先进入大顶堆, 然后又进入小顶堆
        # 如果不这样的话, 小顶堆就没有数字啦
        heapq.heappush(self.big_heap, -num)
        max_num = -heapq.heappop(self.big_heap)
        heapq.heappush(self.small_heap, max_num)

        # 这个操作是为了让左边的大顶堆总是比右边的堆多一个数字
        if len(self.big_heap) < len(self.small_heap):
            min_num = heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, -min_num)


    def findMedian(self):
        if self.count % 2 == 1:
            max_num = -self.big_heap[0]
            return max_num
        else:
            left = -self.big_heap[0]
            right = self.small_heap[0]
            return (left + right) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

aaa = MedianFinder()
aaa.addNum(1)
aaa.addNum(2)
print(aaa.findMedian())     # 1.5
aaa.addNum(3)
print(aaa.findMedian())     # 2