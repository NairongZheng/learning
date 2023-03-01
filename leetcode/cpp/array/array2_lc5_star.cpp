/*
    最长回文子串
    给你一个字符串 s，找到 s 中最长的回文子串。

    思路：
    要是两个for循环的方法，复杂度太高
    找回文串的难点在于，回文串的的长度可能是奇数也可能是偶数，解决该问题的核心是从中心向两端扩散的双指针技巧。
    如果回文串的长度为奇数，则它有一个中心字符；如果回文串的长度为偶数，则可以认为它有两个中心字符。
    (判读回文串是从两边向中间搜索，找回文串是从中心向两边展开)
*/

#include <iostream>
#include <string>
using namespace std;

string palindrome(string s, int l, int r)
{
    while (l >= 0 && r < s.size() && s[l] == s[r])
    {
        l--;
        r++;
    }
    return s.substr(l + 1, r - l - 1);
}

string longestPalindrome(string s)
{
    string result = "";
    for (int i = 0; i < s.size(); i++)
    {
        string s1 = palindrome(s, i, i);
        string s2 = palindrome(s, i, i + 1);
        if (result.size() < s1.size())
        {
            result = s1;
        }
        if (result.size() < s2.size())
        {
            result = s2;
        }
    }
    return result;
}

int main()
{
    string s = "babad";
    string result = longestPalindrome(s);
    cout << result << endl; // bab
    return 0;
}