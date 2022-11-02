/*
    搜索插入位置
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    请必须使用时间复杂度为 O(log n) 的算法。

    (其实就是找到第一个大于等于target的数的位置)
*/
#include <iostream>
#include <vector>
using namespace std;

int searchInsert(vector<int> &nums, int target)
{
    if (nums[nums.size() - 1] < target) // 整个数组都没有大于等于target的，自然就是插到最后
    {
        return nums.size();
    }
    int left = 0;
    int right = nums.size() - 1;
    while (left < right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }
    return left;
}

int main()
{
    vector<int> nums = {1, 3, 5, 6};
    int target = 5;
    int result = searchInsert(nums, target);
    cout << result << endl; // 2
    return 0;
}