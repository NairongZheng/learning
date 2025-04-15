"""
基数排序：
    基数排序按“位”来排序，不比较元素的大小，而是逐位“桶排”：
        从低位到高位（LSD，Least Significant Digit）依次排；
        每一位用稳定排序处理（通常是计数排序）；
        多轮后，整个数组就有序了。
    时间：O(d × (n + k))，d 是最大位数，k 是基数（0-9）
    空间：O(n + k)（额外开桶）
    稳定性：稳定（使用稳定排序算法时）
"""

def counting_sort_by_digit(nums, exp):
    n = len(nums)
    output = [0] * n
    count = [0] * 10  # 基数为10（十进制）

    # 1. 统计当前位的频率
    for num in nums:
        digit = (num // exp) % 10
        count[digit] += 1

    # 2. 前缀和
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3. 倒序遍历稳定填入结果
    for i in reversed(range(n)):
        digit = (nums[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = nums[i]

    return output


def radix_sort(nums):
    if not nums:
        return []

    max_val = max(nums)
    exp = 1 # 默认从个位开始排序
    while max_val // exp > 0:
        nums = counting_sort_by_digit(nums, exp)
        exp *= 10

    return nums


def main():
    nums = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_list = radix_sort(nums)
    print(sorted_list) # [2, 24, 45, 66, 75, 90, 170, 802]


if __name__ == '__main__':
    main()
