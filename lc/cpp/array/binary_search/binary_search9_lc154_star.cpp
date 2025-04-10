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
        if (nums[mid] > nums[right]) // 等号不可以放这里的示例可以看这个[1,3,3]
        {
            left = mid + 1;
        }
        else if (nums[mid] == nums[right]) // 这个等号放到上面还是下面都不行, 所以单独写一个
        {
            right--;
        }
        else // 等号不可以放这里的示例可以看这个[2,2,1,2]
        {
            right = mid;
        }
    }
    return nums[left];
}

int main()
{
    vector<int> nums = {2, 2, 2, 0, 1, 2};
    int result = findMin(nums);
    cout << result << endl; // 0
    return 0;
}