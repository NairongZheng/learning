/*
    寻找重复数
    给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
    假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
    你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

    注意，题目要求不能更改原数组，所以不能排序之后做
    重点！！这个问题使用「二分查找」是在数组 [1, 2,.., n] 中查找一个整数，而 并非在输入数组数组中查找一个整数。
*/

#include <iostream>
#include <vector>
using namespace std;

int findDuplicate(vector<int> &nums)
{
    int left = 1;
    int right = nums.size() - 1;
    while (left < right)
    {
        int mid = left + (right - left) / 2;
        int count = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] <= mid)
            {
                count++;
            }
        }
        if (count > mid)
        {
            right = mid;
        }
        else
        {
            left = mid + 1;
        }
    }
    return left;
}

int main()
{
    vector<int> nums = {1, 2, 5, 2, 3, 4, 6, 2};
    int result = findDuplicate(nums);
    cout << result << endl; // 2
    return 0;
}