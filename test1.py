
import heapq
class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.big_heap = []
        self.count = 0

    def addNum(self, num: int):
        self.count += 1
        heapq.heappush(self.big_heap, -num)
        max_num = -heapq.heappop(self.big_heap)
        heapq.heappush(self.small_heap, max_num)

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