/*
    二分法（迭代）
*/
#include <iostream>
#include <vector>
using namespace std;

void binary_search_1(vector<int> &arr, int target)
{
    int left = 0;
    int right = arr.size() - 1;
    while (left < right)
    {
        int mid = left + (right - left) / 2;    // 跟python版本有点区别，其实这么写比较科学，防止溢出
        if (arr[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }
    if (arr[left] == target)
    {
        cout << "found number in index of " << left << endl;
    }
    else
    {
        cout << "do not have this number in the list" << endl;
    }
}

void binary_search_2(vector<int> &arr, int target)
{
    int left = 0;
    int right = arr.size() - 1;
    while (left < right)
    {
        int mid = left + (right - left + 1) / 2;    // 当出现left==mid的时候, 一定要取右中位数避免死循环, 就是mid = left + (right - left + 1) / 2
        if (arr[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            left = mid;
        }
    }
    if (arr[left] == target)
    {
        cout << "found number in index of " << left << endl;
    }
    else
    {
        cout << "do not have this number in the list" << endl;
    }
}

int main()
{
    vector<int> arr = {0, 1, 2, 3};
    int target = 1;
    binary_search_1(arr, target);
    binary_search_2(arr, target);
    return 0;
}
