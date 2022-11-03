/*
    旋转图像
    给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
    你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
    思路：
    走不寻常的路，用常规的方法去推ij怎么变什么关系，比较复杂，可以用点灵活的方法，镜像、翻转之类的
    这种题要仔细观察
*/

#include <iostream>
#include <vector>
using namespace std;

void rotate_clockwise(vector<vector<int>> &matrix)
{
    int n = matrix.size();
    // 先沿对角线镜像对称矩阵
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // 再左右翻转
    for (int i = 0; i < matrix.size(); i++)
    {
        int left = 0;
        int right = matrix[i].size() - 1;
        while (left < right)
        {
            int temp = matrix[i][left];
            matrix[i][left] = matrix[i][right];
            matrix[i][right] = temp;
            left++;
            right--;
        }
    }
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
    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    rotate_clockwise(matrix);
    printArr(matrix); // [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    return 0;
}