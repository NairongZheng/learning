"""
    滑动窗口最大值
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回 滑动窗口中的最大值。

    思路：用单调队列
    分析一下，队列里的元素一定是要排序的，而且要最大值放在出队口，要不然怎么知道最大值呢。
    但如果把窗口里的元素都放进队列里，窗口移动的时候，队列需要弹出元素。
    那么问题来了，已经排序之后的队列 怎么能把窗口要移除的元素（这个元素可不一定是最大值）弹出呢。
    其实队列没有必要维护窗口里的所有元素，只需要维护有可能成为窗口里最大值的元素就可以了，同时保证队里里的元素数值是由大到小的。!!!!!!!!!!!
    (不要以为实现的单调队列就是 对窗口里面的数进行排序，如果排序的话，那和优先级队列又有什么区别了呢。)
"""

# 解法一：用单调队列
# class MyQueue:
#     def __init__(self):
#         self.queue = []     # 使用list来实现单调队列（从大到小）
    
#     def pop(self, value):
#         """
#             如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作
#         """
#         # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
#         if self.queue and value == self.queue[0]:
#             self.queue.pop(0)
    
#     def push(self, value):
#         """
#             如果push的元素value大于入口元素的数值，那么就将队列入口的元素弹出，直到push元素的数值小于等于队列入口元素的数值为止
#         """
#         # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
#         # 这样就保持了队列里的数值是单调从大到小的了。
#         while self.queue and value > self.queue[-1]:
#             self.queue.pop()
#         self.queue.append(value)
    
#     def front(self):
#         """
#             保持如上push和pop规则，每次窗口移动的时候，只要问que.front()就可以返回当前窗口的最大值。
#         """
#         # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
#         return self.queue[0]

# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         que = MyQueue()
#         result = []
#         for i in range(k):          # 先将前k个元素放进队列
#             que.push(nums[i])
#         result.append(que.front())  # result记录前k的元素的最大值
#         for i in range(k, len(nums)):
#             que.pop(nums[i - k])    # 滑动窗口移除最前面元素
#             que.push(nums[i])       # 滑动窗口加入最后面的元素
#             result.append(que.front())      # 记录对应的最大值
#         return result


# 解法二：用堆(不会)(看看heap7里面的讲解)
class Solution:
    def maxSlidingWindow(self, nums, k):
        import heapq
        que = []
        result = []
        for i in range(k):
            que.append((-nums[i], i))
        heapq.heapify(que)
        result.append(-que[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(que, (-nums[i], i))
            while que[0][1] <= i - k:
                heapq.heappop(que)
            result.append(-que[0][0])
        return result

aaa = Solution()
bbb = aaa.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(bbb)          # [3,3,5,5,6,7]