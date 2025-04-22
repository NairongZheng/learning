"""
归并排序：
    分治思想：
        分解：把数组不断二分，直到每个子数组只剩一个元素；
        解决：递归对每个子数组排序；
        合并：将两个已排序的子数组合并成一个整体有序数组。
    时间：始终 O(nlogn)
    空间：O(n)（需要辅助数组）
    稳定性：稳定（两个相等元素不会因为 merge 而换位置）
"""

def merge(first_list, second_list):
    first_index = 0
    second_index = 0
    result = []
    
    # 按顺序合并
    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] < second_list[second_index]:
            result.append(first_list[first_index])
            first_index += 1
        else:
            result.append(second_list[second_index])
            second_index += 1
    
    result += first_list[first_index:]
    result += second_list[second_index:]
    return result


def merge_sort(nums):
    n = len(nums)
    if n <= 1:          # 递归终止条件
        return nums
    pivot_index = n // 2
    # 递归排序左右子数组
    first_list = merge_sort(nums[:pivot_index])
    second_list = merge_sort(nums[pivot_index:])

    # 合并两个有序数组
    return merge(first_list, second_list)


def main():
    nums = [5, 7, 3, 7, 2]
    sorted_list = merge_sort(nums)
    print(sorted_list) # [2, 3, 5, 7, 7]


if __name__ == '__main__':
    main()