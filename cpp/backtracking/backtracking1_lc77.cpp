/*
    组合
    给定两个整数n和k, 返回范围[1, n]中所有可能的k个数的组合
*/

#include <iostream>
#include <vector>
using namespace std;

// // 用类
// class Solution
// {
// private:
//     vector<vector<int>> result;
//     vector<int> path;
//     void backtracking(int n, int k, int startIndex)
//     {
//         if (path.size() == k)
//         {
//             result.push_back(path);
//             return;
//         }
//         for (int i = startIndex; i < n + 1; i++)
//         {
//             path.push_back(i); // 处理节点
//             backtracking(n, k, i + 1);
//             path.pop_back(); // 回溯，撤销处理的节点
//         }
//     }

// public:
//     vector<vector<int>> combine(int n, int k)
//     {
//         backtracking(n, k, 1);
//         return result;
//     }
// };

// 不用类
void backtracking(int n, int k, int startIndex, vector<vector<int>> &result, vector<int> &path)
{
    if (path.size() == k)
    {
        result.push_back(path);
        return;
    }
    for (int i = startIndex; i < n + 1; i++)
    {
        path.push_back(i); // 处理节点
        backtracking(n, k, i + 1, result, path);
        path.pop_back(); // 回溯，撤销处理的节点
    }
}

vector<vector<int>> combine(int n, int k)
{
    vector<vector<int>> result;
    vector<int> path;
    backtracking(n, k, 1, result, path);
    return result;
}

void printArr(vector<vector<int>> &matrix)
{
    int row = matrix.size();
    int col = matrix[0].size();
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    // // 用类
    // Solution *obj = new Solution();
    // vector<vector<int>> result = obj->combine(4, 2);
    // printArr(result); // [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    // 不用类
    vector<vector<int>> result = combine(4, 2);
    printArr(result); // [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    return 0;
}