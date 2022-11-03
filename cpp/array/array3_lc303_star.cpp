/*
    区域和检索 - 数组不可变
    给定一个整数数组  nums，处理以下类型的多个查询:
    计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
*/

#include <iostream>
#include <vector>
using namespace std;

class NumArray
{
public:
    vector<int> pre_sum = {0};  // 这个要放这里哦，不能放在构造函数里面
    NumArray(vector<int> &nums) // 构造函数，跟python里面的__init__很像。只是变量要放在外面（python的变量可以直接放在init里）。
    {
        for (int i = 1; i < nums.size() + 1; i++)
        {
            pre_sum.push_back(pre_sum[i - 1] + nums[i - 1]);
        }
    }

    int sumRange(int left, int right)
    {
        return pre_sum[right + 1] - pre_sum[left];
    }
};

int main()
{
    vector<int> nums = {-2, 0, 3, -5, 2, -1};
    int left = 0;
    int right = 5;
    NumArray *obj = new NumArray(nums);
    int param_1 = obj->sumRange(left, right);
    cout << param_1 << endl; // -3
    return 0;
}