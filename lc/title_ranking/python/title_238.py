# https://leetcode.cn/problems/product-of-array-except-self/description

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 方法一：俩数组好理解，时间O(n)，空间O(n)
        n = len(nums)
        left_list = [0] * n     # 左侧乘积列表
        right_list = [0] * n    # 右侧乘积列表
        result = [0] * n
        # 开始构建左侧
        left_list[0] = 1
        for i in range(1, n):
            left_list[i] = nums[i - 1] * left_list[i - 1]
        # 开始构建右侧
        right_list[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right_list[i] = nums[i + 1] * right_list[i + 1]
        # 计算结果
        for i in range(n):
            result[i] = left_list[i] * right_list[i]
        return result

        # # 方法二：双指针，时间O(n)，空间O(1)（不算返回数组）
        # result = [1] * len(nums)
        # left, right = 0, len(nums) - 1 # 初始化左右指针
        # lp = 1 # 左侧累积乘积（不包含当前元素）
        # rp = 1 # 右侧累积乘积（不包含当前元素）
        # while left < len(nums) and right >= 0:
        #     result[left] *= lp      # 将当前的左侧累积乘积乘入 result[left]
        #     lp *= nums[left]        # 更新左侧累积乘积（包括当前元素）
        #     result[right] *= rp     # 将当前的右侧累积乘积乘入 result[right]
        #     rp *= nums[right]       # 更新右侧累积乘积（包括当前元素）
        #     left += 1
        #     right -= 1
        # return result
        

def main():
    test_list = [
        [1,2,3,4], # [24,12,8,6]
        [-1,1,0,-3,3], # [0,0,9,0,0]
    ]
    for nums in test_list:
        res = Solution().productExceptSelf(nums)
        print(f"{res}")


if __name__ == '__main__':
    main()