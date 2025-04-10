/*
    寻找旋转排序数组中的最小值
    给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
    你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
*/

#include <iostream>
#include <vector>
using namespace std;

int search(vector<int> &nums, int target)
{
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right)       // 注意这边用的是小于等于，要按照实际情况来的
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target)
        {
            return mid;
        }
        if (nums[0] <= nums[mid])
        {
            if (nums[0] <= target && target < nums[mid])
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        else
        {
            if (nums[mid] < target && target <= nums[nums.size() - 1])
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
    }
    return -1;
}

int main()
{
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int target = 0;
    int result = search(nums, target);
    cout << result << endl; // 4
    return 0;
}