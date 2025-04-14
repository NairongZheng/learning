"""
堆排序：
    利用 堆 这种数据结构来排序，常用的是最大堆（Max Heap）
    1. 建堆：把数组变成一个最大堆（根节点最大）
    2. 排序：
        把堆顶元素（最大值）和最后一个元素交换；
        然后把剩下的部分重新堆化（heapify），重复这个过程直到排序完成。
    时间：O(nlogn)
    空间：O(1)（原地排序）
    稳定性：不稳定（会交换非相邻元素）
"""


def heapify(nums, n, i):
    """
    堆化，用到了下滤
    堆的基础知识可以查看`../../python/heap/heap1_star_star.py`
    """
    largest = i # 当前维护的节点下标为i，假设是最大的
    left = 2 * i + 1  # 左子节点
    right = 2 * i + 2  # 右子节点
    
    # 找到三个节点中最大节点的下标
    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i] # 交换，下标i位置变成三个节点中的最大值
        heapify(nums, n, largest) # 这时候largest就是维护的i的左节点或者右节点，递归向下让每个子树都是大根堆


def heap_sort(nums):
    n = len(nums)
    # 1. 构建最大堆（从最后一个非叶节点开始）
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    # 2. 依次取出堆顶元素放到数组末尾
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]  # 将最大值换到末尾
        heapify(nums, i, 0)  # 重新调整堆
    return nums


def main():
    nums = [5, 7, 3, 7, 2]
    sorted_list = heap_sort(nums)
    print(sorted_list) # [2, 3, 5, 7, 7]


if __name__ == '__main__':
    main()
