/*
    字符串的排列
    给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
    换句话说，s1 的排列之一是 s2 的 子串 。
*/

#include <iostream>
#include <unordered_map> // 要记得加
using namespace std;

bool checkInclusion(string s1, string s2)
{
    unordered_map<char, int> s1_map; // cpp中unordered_map的定义
    for (char c : s1)
    {
        s1_map[c]++;
    }

    int start = 0;
    for (int end = s1.size() - 1; end < s2.size(); end++)
    {
        unordered_map<char, int> s2_map;
        for (char c : s2.substr(start, s1.size()))
        {
            s2_map[c]++;
        }
        if (s2_map == s1_map)
        {
            return true;
        }
        start++;
    }
    return false;
}

int main()
{
    string s1 = "ab";
    string s2 = "eidbaooo";
    bool result = checkInclusion(s1, s2);
    cout << boolalpha << result << endl; // true
    return 0;
}