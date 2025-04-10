/*
    寻找比目标字母大的最小字母
*/
#include <iostream>
#include <vector>
using namespace std;

char nextGreatestLetter(vector<char> &letters, char target)
{
    int n = letters.size();
    if (letters[n - 1] <= target) // 注意c++不能像python一样用-1当下标
    {
        return letters[0];
    }
    int left = 0;
    int right = letters.size() - 1;
    while (left < right)
    {
        int mid = left + (right - left) / 2;
        if (letters[mid] <= target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }
    return letters[left];
}

int main()
{
    vector<char> letters = {'c', 'f', 'j'};
    char target = 'a';
    char result = nextGreatestLetter(letters, target);
    cout << result << endl;
    return 0;
}