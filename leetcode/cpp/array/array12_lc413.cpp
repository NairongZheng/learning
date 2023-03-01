/*
    和为 K 的子数组
    给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
*/

#include <iostream>
#include <vector>
using namespace std;

int cal_n(int n)
{
    /*
        如果有n个连续的等差，那么会有几个子数组
        cons中，对于长度为 n 的等差数列，其所有的长度大于等于3的子数列都是等差数列，则一共有 (n-2)(n-1)/2 个等差数列。
    */
    if (n == 1)
    {
        return 0;
    }
    n += 1;
    return (n - 2) * (n - 1) / 2;
}

int numberOfArithmeticSlices(vector<int> &nums)
{

    // 构建差分数组(跟array5略微有点不同，数组怎么构建根据需求)
    vector<int> diff;
    for (int i = 0; i < nums.size() - 1; i++)
    {
        diff.push_back(nums[i + 1] - nums[i]);
    }

    // 计算有几个是连续的
    vector<int> cons;
    int a = 1;
    for (int i = 1; i < diff.size(); i++)
    {
        if (diff[i] == diff[i - 1])
        {
            a += 1;
        }
        else
        {
            cons.push_back(a);
            a = 1;
        }
    }
    cons.push_back(a);

    // 给出结果
    int result = 0;
    for (int num : cons)
    {
        result += cal_n(num);
    }
    return result;
}

int main()
{
    vector<int> nums = {1, 2, 3, 4, 5, 6, 12, 14, 16};
    int result = numberOfArithmeticSlices(nums);
    cout << result << endl; // 11
}

// nums: [1, 2, 3, 4, 5, 6, 12, 14, 16]
// diff: [1, 1, 1, 1, 1, 6, 2, 2]
// cons: [5, 1, 2]