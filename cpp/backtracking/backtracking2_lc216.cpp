/*
    组合总和III
    找出所有相加之和为n的k个数的组合, 且满足下列条件:
    只使用数字1到9
    每个数字最多使用一次
    返回所有可能的有效组合的列表. 该列表不能包含相同的组合两次, 组合可以以任何顺序返回
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
private:
    vector<int> path;
    vector<vector<int>> result;
    void backtracking(int k, int n, int startIndex, int sum_)
    {
        if (path.size() == k)
        {
            if (sum_ == n)
            {
                result.push_back(path);
            }
            return;
        }
        for (int i = startIndex; i < 10; i++)
        {
            path.push_back(i);
            sum_ += i;
            backtracking(k, n, i + 1, sum_);
            sum_ -= i;
            path.pop_back();
        }
    }

public:
    vector<vector<int>> combinationSum3(int k, int n)
    {
        backtracking(k, n, 1, 0);
        return result;
    }
};

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
    Solution *obj = new Solution();
    vector<vector<int>> result = obj->combinationSum3(3, 9);
    printArr(result); // [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
}