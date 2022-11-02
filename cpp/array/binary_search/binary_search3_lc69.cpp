/*
    x的平方根
*/
#include <iostream>
using namespace std;

int mySqrt(int x)
{
    int left = 0;
    int right = x / 2 + 1;
    while (left < right)
    {
        long mid = left + (right - left + 1) / 2; // 因为测试用例中有比较大的值，用int会溢出，所以用long
        if (mid * mid > x)                        // 用int的话，在这句mid*mid会溢出
        {
            right = mid - 1;
        }
        else
        {
            left = mid;
        }
    }
    return left;
}

int main()
{
    int x = 13;
    int result = mySqrt(x);
    cout << x << "的平方根是" << result << endl;
    return 0;
}