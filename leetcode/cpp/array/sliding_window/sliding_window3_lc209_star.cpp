/*
    字符串的排列
    给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
    换句话说，s1 的排列之一是 s2 的 子串 。
*/

#include <iostream>
#include <vector>
using namespace std;

int minSubArrayLen(int target, vector<int> &nums)
{
    int start = 0;
    int cur_sum = 0;
    int min_len = INT_MAX;
    for (int end = 0; end < nums.size(); end++)
    {
        cur_sum += nums[end];
        while (cur_sum >= target)
        {
            min_len = min(min_len, end - start + 1);
            cur_sum -= nums[start];
            start += 1;
        }
    }
    if (min_len == INT_MAX)
    {
        return 0;
    }
    else
    {
        return min_len;
    }
}
int main()
{
    int target = 7;
    vector<int> nums = {2, 3, 1, 2, 4, 3};
    int result = minSubArrayLen(target, nums);
    cout << result << endl; // true
    return 0;
}