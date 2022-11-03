/*
    找出字符串中第一个匹配项的下标
*/

#include <iostream>
using namespace std;

int strStr(string haystack, string needle)
{
    int start = 0;
    for (int end = needle.size() - 1; end < haystack.size(); end++)
    {
        if (haystack.substr(start, needle.size()) == needle)    // s.substr(pos, size)，取字符串s的子串，从pos位置开始，取size长度
        {
            return start;
        }
        start++;
    }
    return -1;
}


int main()
{
    string haystack = "hello";
    string needle = "ll";
    int result = strStr(haystack, needle);
    cout << result << endl; // 2
    return 0;
}