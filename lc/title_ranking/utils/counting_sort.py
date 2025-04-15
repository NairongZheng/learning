"""
计数排序：
    计数排序适用于整数、范围有限、重复多的场景。
        统计频率：创建一个计数数组 count[]，每个元素记录原数组中该值的出现次数；
        累加前缀和：将计数数组转换为前缀和数组，表示小于等于某值的元素有多少个；
        填入新数组：从原数组倒序遍历，根据 count[x] 找到该值在输出数组中的位置，放入。
        （后面两个步骤是为了保证顺序，即排序后的稳定性）
    时间：O(n + k)，其中 k 是值域大小
    空间：O(k)（开了一个计数数组）
    稳定性：稳定（从后往前填回原数组可保持顺序）
"""

def counting_sort(nums):                    # [5, 7, 3, 7, 2]
    if not nums:
        return []

    max_val = max(nums)
    count = [0] * (max_val + 1)

    # 1. 统计频率
    for num in nums:
        count[num] += 1                     # [0, 0, 1, 1, 0, 1, 0, 2]

    # 2. 构建前缀和（累计频率）
    for i in range(1, len(count)):          # [0, 0, 1, 2, 2, 3, 3, 5]
        # 这个前缀和数组的含义是：值为 i 的元素，在最终排序结果中，应该放在索引 count[i] - 1 的位置（也就是前面有多少个元素 ≤ i）。
        count[i] += count[i - 1]

    # 3. 回填结果数组（必须倒序才能保持稳定性）
    output = [0] * len(nums)
    for num in reversed(nums):
        count[num] -= 1
        output[count[num]] = num

    return output


def main():
    nums = [5, 7, 3, 7, 2]
    sorted_list = counting_sort(nums)
    print(sorted_list) # [2, 3, 5, 7, 7]


if __name__ == '__main__':
    main()
