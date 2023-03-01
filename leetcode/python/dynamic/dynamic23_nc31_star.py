

# 看不太懂
"""
    最长上升子序列(三)
    给定数组 arr ，设长度为 n ，输出 arr 的最长上升子序列。
    （如果有多个答案，请输出其中 按数值(注：区别于按单个字符的ASCII码值)进行比较的 字典序最小的那个）
    要求：空间复杂度 O(n)，时间复杂度 O(nlogn)
"""
class Solution:
    def LIS(self , arr):
        # write code here
        dp = [0 for _ in range(len(arr))]   # dp[i]表示以arr[i]为结尾的最长上升子序列的长度
        dp[0] = 1
        minele_res = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] > minele_res[-1]:
                minele_res.append(arr[i])
                dp[i] = len(minele_res)
            else:
                pos = self.BinSearch(minele_res, arr[i])
                minele_res[pos] = arr[i]
                dp[i] = pos + 1
        length = len(minele_res)
        for i in range(len(arr) - 1, -1, -1):       # 这里就看不是很懂
            if dp[i] == length:
                minele_res[length - 1] = arr[i]
                length -= 1
        return minele_res
    
    def BinSearch(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

aaa = Solution()
bbb = aaa.LIS([2,1,5,3,6,4,8,9,7])
print(bbb)      # [1, 3, 4, 8, 9]

# dp: [1, 1, 2, 2, 3, 3, 4, 5, 4]