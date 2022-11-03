/*
    拼车
    车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
    给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，
    接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
    当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
    0 <= fromi < toi <= 1000
*/

#include <iostream>
#include <vector>
using namespace std;

bool carPooling(vector<vector<int>> &trips, int capacity)
{
    vector<int> diff;
    diff.resize(1001); // 可以这么初始化
    for (vector<int> trip : trips)
    {
        int val = trip[0];
        int i = trip[1];
        int j = trip[2];
        diff[i] += val;
        if (j < diff.size())
        {
            diff[j] -= val; // 注意题目说的，从to就会下车，所以跟之前的题目不一样，不是在j+1的地方减，而是在j的地方
        }
    }
    vector<int> result(diff.size()); // 也可以这么初始化
    result[0] = diff[0];
    for (int i = 1; i < result.size(); i++)
    {
        result[i] = result[i - 1] + diff[i];
        if (result[i] > capacity)
        {
            return false;
        }
    }
    if (result[0] > capacity)
    {
        return false;
    }
    return true;
}

int main()
{
    vector<vector<int>> trips = {{2, 1, 5}, {3, 3, 7}};
    int capacity = 4;
    bool result = carPooling(trips, capacity);
    cout << boolalpha << result << endl; // false
    return 0;
}