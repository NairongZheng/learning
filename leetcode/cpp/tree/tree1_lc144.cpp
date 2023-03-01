/*
    二叉树的前序遍历
    (中左右)
*/
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// // 递归法
// class Solution
// {
// public:
//     void traversal(TreeNode *tree, vector<int> &result)
//     {
//         if (tree == NULL)
//             return;
//         result.push_back(tree->val);
//         traversal(tree->left, result);
//         traversal(tree->right, result);
//     }

//     vector<int> preorderTraversal(TreeNode *root)
//     {
//         vector<int> result;
//         traversal(root, result);
//         return result;
//     }
// };

// 迭代法
class Solution
{
public:
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> result;
        stack<TreeNode *> st;
        if (root != NULL)
        {
            st.push(root);
        }
        while (!st.empty())
        {
            TreeNode *node = st.top();
            if (node != NULL)
            {
                st.pop();
                if (node->right) st.push(node->right); // 右
                if (node->left) st.push(node->left); // 左
                st.push(node);           // 中
                st.push(NULL);
            }
            else
            {
                st.pop();
                node = st.top();
                st.pop();
                result.push_back(node->val);
            }
        }
        return result;
    }
};

void printArr(vector<int> &arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    TreeNode *node7 = new TreeNode(8);
    TreeNode *node6 = new TreeNode(7);
    TreeNode *node5 = new TreeNode(2);
    TreeNode *node4 = new TreeNode(1);
    TreeNode *node3 = new TreeNode(6, node6, node7);
    TreeNode *node2 = new TreeNode(4, node4, node5);
    TreeNode *node1 = new TreeNode(5, node2, node3);
    Solution *obj = new Solution();
    vector<int> result = obj->preorderTraversal(node1);
    printArr(result); // 5 4 1 2 6 7 8
    return 0;
}