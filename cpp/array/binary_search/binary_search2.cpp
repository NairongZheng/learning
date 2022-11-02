/*
    二分法（递归）
*/
#include <iostream>
#include <vector>
using namespace std;
void binary_search(vector<int> &arr, int left, int right, int target)
{
    if (left == right)
    {
        if (arr[left] == target)
        {
            cout << "found number in index of " << left << endl;
        }
        else
        {
            cout << "do not have this number in the list" << endl;
        }
        return;
    }
    int mid = left + (right - left) / 2;
    if (arr[mid] < target)
    {
        binary_search(arr, mid + 1, right, target);
    }
    else
    {
        binary_search(arr, left, mid, target);
    }
}
int main()
{
    vector<int> arr = {0, 1, 2, 3};
    int target = 1;
    binary_search(arr, 0, 3, target);   // found number in index of 1
    return 0;
}