/*
    K 个不同整数的子数组
    给定一个正整数数组nums和一个整数k, 返回num中'好子数组'的数目。
    如果nums的某个子数组中不同整数的个数恰好为k, 则称nums的这个连续、不一定不同的子数组为'好子数组'
    例如, [1,2,3,1,2] 中有 3个不同的整数:1,2,以及3。
    子数组是数组的连续部分。

    恰好为k!!!!!!!!  904题就是小于等于, 而这题是等于. 只取等于的话就比较复杂
    其实等于就要涉及滑动窗口回缩, 但是可以用<=k 的结果减去 <=(k-1)的结果, 就是刚好等于k了
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int leK(vector<int> &nums, int k)
{
    int start = 0;
    unordered_map<int, int> adict;
    int count = 0;
    for (int end = 0; end < nums.size(); end++)
    {
        adict[nums[end]]++;
        while (adict.size() > k)
        {
            adict[nums[start]]--;
            if (adict[nums[start]] == 0)
            {
                adict.erase(nums[start]);
            }
            start++;
        }
        count += (end - start + 1);
    }
    return count;
}

int subarraysWithKDistinct(vector<int> &nums, int k)
{
    return leK(nums, k) - leK(nums, k - 1);
}

int main()
{
    vector<int> nums = {1, 2, 1, 2, 3};
    int k = 2;
    int result = subarraysWithKDistinct(nums, k);
    cout << result << endl; // 7
    return 0;
}