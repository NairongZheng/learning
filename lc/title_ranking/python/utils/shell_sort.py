"""
希尔排序：
    是插入排序的改进版：先按一定“间隔”对数组进行分组排序，然后逐步缩小间隔，最后变为普通插入排序。
    目的是提前让数据基本有序，加快插入排序的速度。
    时间复杂度取决于间隔序列，常见是 n/2 不断除以 2
    时间：最坏 O(n²)，最好 O(nlogn)
    空间：O(1)
    稳定性：不稳定
"""

def shell_sort(nums):
    gap = len(nums) // 2
    while gap >= 1:
        for i in range(gap, len(nums)):
            while i > 0: # 类似插入排序，只是每次跳 gap 步
                if nums[i] < nums[i - gap]:
                    nums[i], nums[i - gap] = nums[i - gap], nums[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return nums


def main():
    nums = [5, 7, 3, 7, 2]
    sorted_list = shell_sort(nums)
    print(sorted_list) # [2, 3, 5, 7, 7]


if __name__ == '__main__':
    main()