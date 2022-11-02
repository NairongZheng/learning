#include <iostream>
#include <vector>
using namespace std;

void binary_search_1(vector<int> &arr, int target)
{
    int left = 0;
    int right = arr.size() - 1;
    while (left < right)
    {
        int mid = left + (right - left) / 2;
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

int main()
{
    vector<int> arr = {0, 1, 2, 3};
    int target = 5;
    binary_search_1(arr, target);
    return 0;
}
