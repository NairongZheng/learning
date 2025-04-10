

def findLength(nums1, nums2):
    """
        最长重复子数组
        给两个整数数组 A 和 B, 返回两个数组中公共的, 长度最长的子数组的长度
    """

    # dp[i][j]定义: 以下标i - 1为结尾的A, 和以下标j - 1为结尾的B, 最长重复子数组长度为dp[i][j]
    # 根据dp[i][j]的定义, dp[i][0]和dp[0][j]其实都是没有意义的.
    dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
    result = 0
    for i in range(1, len(nums1) + 1):
        for j in range(1, len(nums2) + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])
    return result

aaa = findLength([1,2,3,2,1], [3,2,1,4,7])
print(aaa)