# array数组或者字符串
- [参考链接](https://labuladong.online/algo/essential-technique/array-two-pointers-summary-2)
- sliding_window：滑动窗口
- binary_srarch：二分查找
- sorting：排序相关算法

1. 删除有序数组中的重复项
2. 最长回文子串
3. 区域和检索 - 数组不可变
4. 二维区域和检索 - 矩阵不可变
5. 差分数组工具类
6. 航班预定统计
7. 拼车
8. 旋转图像
9. 螺旋矩阵
10. 螺旋矩阵II
11. [和为K的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/solution/python3-by-wu-qiong-sheng-gao-de-qia-non-w6jw/)
12. 等差数列划分

#### 1. 双指针
- 快慢指针：array1、listnode7、lc27、lc283、滑动窗口
- 左右指针：二分查找、lc167、lc344、array2
#### 2. 前缀和数组
- 前缀和主要适用的场景是原始数组不会被修改的情况下，频繁查询某个区间的累加和。
- 一般前缀和要是一维数组就在前面多个0，二维就多一圈。防止在计算的时候判断边界条件麻烦
- array3、array4、array11
#### 3. 差分数组
- 差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减(这个数组是可以反推回nums数组的！！！)
- 一般差分数组就跟nums一样长就可以了
- 比如说，我给你输入一个数组 nums，然后又要求给区间 nums[2, 6] 全部加 1，再给 nums[3, 9] 全部减 3，再给 nums[0, 4] 全部加 2，再给….然后问你，最后 nums 数组的值是什么？
- 常规的思路是循环加，但是这样效率太低了，可以用差分数组的方法解决
- 如果你想对区间 nums[i, j] 的元素全部加 3，那么只需要让 diff[i] += 3，然后再让 diff[j+1] -= 3 即可。原理很简单，回想 diff 数组反推 nums 数组的过程，diff[i] += 3 意味着给 nums[i:] 所有的元素都加了 3，然后 diff[j+1] -= 3 又意味着对于 nums[j+1:] 所有元素再减 3，那综合起来，是不是就是对 nums[i, j] 中的所有元素都加 3 了？
- array5、array6、array7、array12
