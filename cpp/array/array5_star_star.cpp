/*
    差分数组工具类
*/

#include <iostream>
#include <vector>
using namespace std;

class Difference
{
public:
    vector<int> diff;
    Difference(vector<int> &nums) // 构造差分数组
    {
        int n = nums.size();
        diff.resize(n);
        diff[0] = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            diff[i] = nums[i] - nums[i - 1];
        }
    }
    void increment(int i, int j, int val) // 给闭区间[i, j]，对这个区间内的所有数增加val
    {
        diff[i] += val;
        if (j + 1 < diff.size())
        {
            diff[j + 1] -= val;
        }
    }
    vector<int> return_result()
    {
        vector<int> result;
        result.resize(diff.size());
        result[0] = diff[0];
        for (int i = 1; i < diff.size(); i++)
        {
            result[i] = result[i - 1] + diff[i];
        }
        return result;
    }
};

void printArr(vector<int> &arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    vector<int> nums = {0, 1, 2, 3, 4, 5, 6, 7};
    Difference *obj = new Difference(nums); // diff: [0, 1, 1, 1, 1, 1, 1, 1]
    obj->increment(0, 4, 2);                // diff: [2, 1, 1, 1, 1, -1, 1, 1]
    obj->increment(3, 6, -1);               // diff: [2, 1, 1, 0, 1, -1, 1, 2]
    vector<int> result = obj->return_result();
    printArr(result); // [2, 3, 4, 4, 5, 4, 5, 7]
    return 0;
}