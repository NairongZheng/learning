
# cpp这是c++版本
1. array-binary_search-binary_search1：vector的定义及传参
2. array-binary_search-binary_search3：二分查找的mid怎么定义
3. array-binary_search-binary_search4：数组下标不能有负数
4. array-sliding_window-sliding_window0：无穷大无穷小怎么表示(INT_MIN)，set的使用
5. array-sliding_window-sliding_window1：字符串取子串
6. array-sliding_window-sliding_window4：map/unordered_map的定义，删除
7. array-array3：类的定义及使用(也可以看看backtracking1)
8. array-array4：二维vector的初始化及使用
9. array-array7：vector的初始化！
10. listnode-listnode1：链表
11. tree-tree1：树


```cpp
// 链表定义
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
```

```cpp
// 树定义
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
```