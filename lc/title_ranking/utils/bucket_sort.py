"""
桶排序：
    桶排序把数据划分到不同的“桶”中，每个桶内的数据再单独排序，最后把所有桶连接起来。适用于：
        数据均匀分布；
        有实数/浮点数时表现尤其优秀；
        也适合大量分散的整数（可以控制桶大小）。
    关键步骤：
        创建桶（bucket）：按范围划分成若干个区间；
        分桶：把每个元素放入对应的桶中；
        桶内排序：每个桶内部用排序（比如插入排序、快排等）；
        合并桶：把所有桶按顺序合并成一个完整的数组。
    时间：最坏 O(n²)，最好 O(n)，平均 O(n + k)
    空间：O(n + k)，k 是桶的数量
    稳定性：稳定（如果桶内排序用稳定排序算法）
"""

def bucket_sort(nums):
    if not nums:
        return []
    
    # 找到最大值跟最小值
    min_val = float('inf')
    max_val = -float('inf')
    for num in nums:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    
    # 设置桶个数跟大小
    n = len(nums)
    bucket_size = (max_val - min_val) // n + 1 # 需要保证至少有一个桶，故而需要加个1
    bucket_cnt = (max_val - min_val) // bucket_size + 1 # 求得了size即知道了每个桶所装数据的范围，还需要计算出所需的桶的个数cnt
    buckets = [[] for _ in range(bucket_cnt)]
    
    # 1. 分桶
    # 求得了size和cnt后，即可知第一个桶装的数据范围为 [min_val, min_val + size)，第二个桶为 [min_val + size, min_val + 2 * size)，…，以此类推
    for i in range(n):
        num = nums[i]
        bucket_idx = (num - min_val) // bucket_size
        buckets[bucket_idx].append(num) # [[3, 6, 9, 1, 1], [10], [], [34], [], [], [], [67]]

    # 2. 桶内排序（可以选用插入排序/内建排序）
    for bucket in buckets:
        bucket.sort()

    # 3. 合并所有桶
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


def main():
    nums = [3, 6, 9, 1, 1, 10, 67, 34]
    sorted_list = bucket_sort(nums)
    print(sorted_list) # [1, 1, 3, 6, 9, 10, 34, 67]


if __name__ == '__main__':
    main()
