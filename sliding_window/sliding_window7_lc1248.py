

from itertools import count


def numberOfSubarrays(nums, k):
    """
        统计'优美子数组'
    """

    def ltK(nums, k):
        """
            找到小于等于k个的
        """
        start = 0
        count_odd = 0
        count = 0
        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                count_odd += 1
            while count_odd > k:
                if nums[start] % 2 == 1:
                    count_odd -= 1
                start += 1
            count += (end - start + 1)
        return count
    return ltK(nums, k) - ltK(nums, k - 1)

aaa = numberOfSubarrays([1,1,2,1,1], 3)
print(aaa)