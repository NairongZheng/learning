/*
    在排序数组中查找元素的第一个和最后一个位置
    给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
    如果数组中不存在目标值 target，返回 [-1, -1]。
    你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
*/
#include <iostream>
#include <vector>
using namespace std;

vector<int> searchRange(vector<int> &nums, int target)
{
    vector<int> result = {-1, -1};
    if (nums.size() == 0)
    {
        return result;
    }

    // 找左边界（就是找到第一个大于等于target的位置）
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
    if (nums[left] != target) // 第一个大于等于target的数不是target的话，说明里面没有target
    {
        return result;
    }
    result[0] = left;

    // 找右边界（就是找到最后一个小于等于target的位置）
    left = 0;       // 注意这边就不要加int了，会重复声明错误
    right = nums.size() - 1;
    while (left < right)
    {
        int mid = left + (right - left + 1) / 2;
        if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            left = mid;
        }
    }
    result[1] = left;
    return result;
}

int main()
{
    vector<int> nums = {6, 7, 7, 8, 8, 8, 20};
    int target = 8;
    vector<int> result = searchRange(nums, target);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl; // [3, 5]
    return 0;
}