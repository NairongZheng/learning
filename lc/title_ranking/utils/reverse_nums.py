


def reverse(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
    

def main():
    nums = [1,2,3,4,5]
    reverse(nums)
    print(nums)


if __name__ == '__main__':
    main()