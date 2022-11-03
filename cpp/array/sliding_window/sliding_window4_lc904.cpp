/*
    水果成篮
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int totalFruit(vector<int> &fruits)
{
    int start = 0;
    int max_len = INT_MIN;
    unordered_map<int, int> adict;
    for (int end = 0; end < fruits.size(); end++)
    {
        adict[fruits[end]]++;
        while (adict.size() > 2)
        {
            adict[fruits[start]]--;
            if (adict[fruits[start]] == 0)
            {
                adict.erase(fruits[start]); // 注意这里跟python的删除方法有点区别
            }
            start++;
        }
        max_len = max(max_len, end - start + 1);
    }
    if (max_len == INT_MIN)
    {
        return 0;
    }
    else
    {
        return max_len;
    }
}

int main()
{
    vector<int> fruits = {1, 2, 3, 2, 2};
    int result = totalFruit(fruits);
    cout << result << endl; // 4
    return 0;
}