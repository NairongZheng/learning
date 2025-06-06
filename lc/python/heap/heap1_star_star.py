"""
    两个代码：
    一个实现了大根堆类（也可以小根堆，改一下大于等于就行）（主要看这个）
    另一个实现堆排序，只要第一个会了就行
"""

# 代码一
class myHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):      # 用到了上滤
        """往堆中添加元素"""
        self.heap.append(x)
        index = len(self.heap) - 1
        while index > 0:
            father_index = (index - 1) // 2
            if self.heap[father_index] < x:
                self.heap[father_index], self.heap[index] = self.heap[index], self.heap[father_index]
            index = father_index

    def heapify(self, n, i):    # 用到了下滤
        """堆化"""
        largest = i             # 当前维护的节点下标为i，假设是最大的
        left = 2 * i + 1        # 左节点
        right = 2 * i + 2       # 右节点

        # 找到三个节点中最大节点的下标
        if left <= n and self.heap[largest] < self.heap[left]:
            largest = left
        if right <= n and self.heap[largest] < self.heap[right]:
            largest = right
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]     # 交换，下标i位置变成三个节点中的最大值
            self.heapify(n, largest)   # 这时候largest就是维护的i的左节点或者右节点，递归继续向下让每个子树都是大根堆
    
    def pop(self):
        """弹出堆顶元素"""
        index = len(self.heap) - 1
        self.heap[0], self.heap[index] = self.heap[index], self.heap[0]
        tmp = self.heap.pop()
        self.heapify(len(self.heap) - 1, 0)
        return tmp


def main():
    aaa = myHeap()
    aaa.push(1)
    aaa.push(7)
    aaa.push(2)
    aaa.push(10)
    aaa.push(7)
    aaa.push(5)
    aaa.push(4)
    a1 = aaa.pop()
    a2 = aaa.pop()
    print(a1, a2)       # 10 7


if __name__ == '__main__':
    main()


# 堆的基本知识
# 堆是一个完全二叉树(只允许最后一排不满，且最后一行必须从左往右排，元素之间不可以有间隔)
# 大根堆：父节点 > 子节点；小根堆：父节点 < 子节点

#     大根堆                  小根堆
#       10                      1
#   7       7               2       3
# 4   5   1   2           5   6   10  12

# 存储方式：放在数组中即可，从上到下从左到右，就是二叉树的层序遍历
# 节点下标为i，左子节点下标为2i+1，右子节点下标为2i+2，父节点下标为(i-1)//2

# 堆的下滤：O(logN)
# 堆的上滤：O(logN)

# 大根堆举例
# 自顶向下建堆法：(1)一个个插入堆，就是放到最后一位; (2)然后上滤操作
# 自下而上建堆法：从倒数第二排开始，对每个父节点进行下滤操作



# # 代码二
# def heapify(nums, n, i):
#     """
#         自下向上构建大根堆
#         维护i节点及以下的节点(到n)为大根堆
#     """
#     largest = i             # 当前维护的节点下标为i，假设是最大的
#     left = 2 * i + 1        # 左节点
#     right = 2 * i + 2       # 右节点

#     # 找到三个节点中最大节点的下标
#     if left < n and nums[largest] < nums[left]:
#         largest = left
#     if right < n and nums[largest] < nums[right]:
#         largest = right
    
#     if largest != i:
#         nums[i], nums[largest] = nums[largest], nums[i]     # 交换，下标i位置变成三个节点中的最大值
#         heapify(nums, n, largest)   # 这时候largest就是维护的i的左节点或者右节点，递归继续向下让每个子树都是打根堆


# def heap_sort(nums):
#     print('原始数组：', nums)

#     # 构建大根堆
#     for i in range(len(nums) - 1, -1, -1):
#         heapify(nums, len(nums), i)
#     print('变成大根堆：', nums)

#     # 堆排序
#     for i in range(len(nums) - 1, 0, -1):
#         nums[i], nums[0] = nums[0], nums[i]
#         heapify(nums, i, 0)         # 因为是大根堆，所以把最大的值和最后一个值做交换，然后维护除最后一个值之外为大根堆，如此循环，结束就是递增数组
#     print('排序后：', nums)

# if __name__ == '__main__':
#     nums = [5, 4, 2, 1, 10, 7, 7]
#     heap_sort(nums)
#     # 原始数组： [5, 4, 2, 1, 10, 7, 7]
#     # 变成大根堆： [10, 5, 7, 1, 4, 2, 7]
#     # 排序后： [1, 2, 4, 5, 7, 7, 10]