/*
    二维区域和检索 - 矩阵不可变
    给定一个二维矩阵 matrix，以下类型的多个请求：
    计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
*/

#include <iostream>
#include <vector>
using namespace std;

class NumMatrix
{
public:
    vector<vector<int>> pre_sum; // 二维vector的定义，整体是个vector，里面的每个元素也都是vector，再里面的每个元素是int
    NumMatrix(vector<vector<int>> &matrix)
    {
        int m = matrix.size();
        int n = matrix[0].size();
        // 其实就是python中的self.presum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]。（cpp这里的默认值会用0填充）
        pre_sum.resize(m + 1, vector<int>(n + 1)); // 要先resize，因为定义的时候是空的，不resize的话，下面pre_sum[i][j]赋值会报错
        for (int i = 1; i < m + 1; i++)
        {
            for (int j = 1; j < n + 1; j++)
            {
                pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1] + matrix[i - 1][j - 1];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2)
    {
        return pre_sum[row2 + 1][col2 + 1] - pre_sum[row1][col2 + 1] - pre_sum[row2 + 1][col1] + pre_sum[row1][col1];
    }
};

int main()
{
    vector<vector<int>> matrix = {{3, 0, 1, 4, 2},
                                  {5, 6, 3, 2, 1},
                                  {1, 2, 0, 1, 5},
                                  {4, 1, 0, 1, 7},
                                  {1, 0, 3, 0, 5}};
    NumMatrix *obj = new NumMatrix(matrix);
    int param_1 = obj->sumRegion(1, 2, 2, 4);
    cout << param_1 << endl; // 12
    return 0;
}