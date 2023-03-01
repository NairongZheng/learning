/*
    无重复字符的最长子串
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
*/

#include <iostream>
#include <limits.h>     // 好像不用包含就可以用INT_MAX了
#include <set>
using namespace std;

int lengthOfLongestSubstring(string s)
{
    int start = 0;
    int max_len = INT_MIN; // int无穷大用INT_MAX表示，无穷小用INT_MIN表示
    set<int> mark;
    for (int end = 0; end < s.size(); end++)
    {
        while (mark.find(s[end]) != mark.end()) // 元素是否在集合中
        {
            mark.erase(s[start]);   // 删除集合中的元素
            start++;
        }
        max_len = max(max_len, end - start + 1);
        mark.insert(s[end]);    // 往集合中添加元素
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
    string s = "abcabcbb";
    int target = 0;
    int result = lengthOfLongestSubstring(s);
    cout << result << endl; // 3
    return 0;
}