/*
    和为 K 的子数组
    给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
    方法四：前缀和+哈希表(看不是很懂)
    优化方法：边算前缀和边统计，统计每一个前缀和出现的个数，然后计算到i位置（含i）的前缀和presum减去目标k在历史上出现过几次
    假如出现过m次，代表第i位以前（不含i）有m个连续子数组的和为presum-k，这m个和为presum-k的连续子数组
    每一个都可以和presum组合成presum-(presum-k)=k
*/
int subarraySum(vector<int> &nums, int k)
{
    int result = 0;
    unordered_map<int, int> pre_sum_dict;
    pre_sum_dict[0] = 1;

    int pre_sum = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        pre_sum += nums[i];
        result += pre_sum_dict[pre_sum - k];
        pre_sum_dict[pre_sum] += 1;
    }
    return result;
}

int main()
{
    vector<int> nums = {2, -2, 3, 0, 4, -7};
    int k = 0;
    int result = subarraySum(nums, k);
    cout << result << endl; // 4
}