/*
    寻找旋转排序数组中的最小值
    给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
    你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
*/

#include <iostream>
#include <vector>
using namespace std;

int findMin(vector<int> &nums)
{
    int left = 0;
    int right = nums.size() - 1;
    while (left < right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[right])
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }
    return nums[left];
}

int main()
{
    vector<int> nums = {3, 5, 4, 1, 2};
    int result = findMin(nums);
    cout << result << endl; // 1
    return 0;
}