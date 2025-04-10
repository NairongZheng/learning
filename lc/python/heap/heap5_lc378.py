
# 注意与3的区别

"""
    有序矩阵中第 K 小的元素
    给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
    请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
    你必须找到一个内存复杂度优于 O(n^2) 的解决方案。

    思路：
    要找第k小的，就需要堆保存k个最小的值，堆顶的这k个中最大的，所以用大根堆
    为什么不能像heap3那样用小根堆弹k次？
    因为将整个矩阵构建成小根堆需要的空间复杂度是O(n^2)，不满足题目要求
"""

import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        maxheap = []    # 最大堆。用最大堆保存最小的k个数，堆顶就是第k小的数。
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(maxheap) < k:
                    heapq.heappush(maxheap, -matrix[i][j])
                elif matrix[i][j] < -maxheap[0]:        # 堆已经满k个之后，再来新的数就看看它与堆顶的大小，小的话就替换进去
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap, -matrix[i][j])
                else:               # 大的话，因为矩阵行有序，所以本行后面的肯定也大，直接break，看看下一行
                    break
        return -maxheap[0]

aaa = Solution()
bbb = aaa.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
print(bbb)      # 13