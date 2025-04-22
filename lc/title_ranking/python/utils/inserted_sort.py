"""
插入排序：
    从第二个数开始，插入到前面已经排好序的那一部分。
    时间：最坏 O(n²)，最好 O(n)
    空间：O(1)
    稳定性：稳定
"""

def inserted_sort(nums):
    for i in range(1, len(nums)):
        while i > 0:
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
            else:
                break
    return nums


def main():
    nums = [5, 7, 3, 7, 2]
    sorted_list = inserted_sort(nums)
    print(sorted_list) # [2, 3, 5, 7, 7]


if __name__ == '__main__':
    main()