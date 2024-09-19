import pandas as pd
import numpy as np


class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.DataFrame()

    def read_csv(self, is_header=False):
        """
        读取 CSV 文件，并返回其中的内容
        """
        try:
            if not is_header:
                df = pd.read_csv(self.file_path, header=None)
            else:
                df = pd.read_csv(self.file_path)
            return df
        except FileNotFoundError:
            print("文件不存在")
            return pd.DataFrame()

    def write_csv(self, is_index=False, is_header=False):
        """
        将数据写入 CSV 文件
        """
        self.df.to_csv(self.file_path, index=is_index, header=is_header)
    
    def shuffle_df(self):
        self.df = self.df.sample(frac=1)
    
    def get_row_col(self):
        """
        获取行数跟列数
        """
        return self.df.shape
    
    def generate_df(self, size, low=5000, high=1000000):
        """
        生成指定行列的df
        """
        new_df_data = np.random.randint(low, high, size)
        new_df = pd.DataFrame(new_df_data)
        return new_df
    
    def concat_df(self, new_rows_df, axis=0):
        """
        拼接两个df
        axis: 0为行拼接, 1为列拼接
        """
        self.df = pd.concat([self.df, new_rows_df], ignore_index=True, axis=axis)
    
    def drop_df(self, drop_idx, axis=0):
        """
        删除某行或者某列
        """
        if axis == 0:
            self.df = self.df.reset_index(drop=True) # 对行重新编号
            self.df = self.df.drop(index=drop_idx)
            self.df = self.df.reset_index(drop=True) # 对行重新编号
        elif axis == 1:
            self.df = self.df.drop(columns=drop_idx)
        pass
    
    def sort_df(self):
        """用 index 排序"""
        self.df = self.df.sort_index()
        pass

    def df_proc(self):
        """
        分组示例
        """
        new_df = pd.DataFrame()
        group_by_flag = self.df.groupby(self.df.iloc[:, -1])    # 用最后一列进行分组
        for group_name, group_df in group_by_flag:
            if group_name == 0:
                group_df.iloc[:, :-2] /= 100
            elif group_name == 1:
                group_df.iloc[:, :-2] *= 100
            new_df = pd.concat([new_df, group_df], axis=0)
        self.df = new_df

    def parse(self):
        # # 读csv
        # self.df = self.read_csv(is_header=True)
        # 生成df
        self.df = self.generate_df(size=(3, 6))
        # 获取行列
        row, col = self.get_row_col()
        # 生成几行
        new_row_df = self.generate_df(size=(3, self.df.shape[1]))
        # 拼接
        self.concat_df(new_row_df, axis=0)
        # 生成几列
        new_col_df = self.generate_df(size=(self.df.shape[0], 2), low=0, high=2)
        # 拼接
        self.concat_df(new_col_df, axis=1)
        # 分组筛选操作
        self.df_proc()
        # 排序
        self.sort_df()
        # 打乱
        self.shuffle_df()
        # 删除某行
        self.drop_df(3)
        # 删除某列
        self.drop_df(3, axis=1)
        # # 写入
        # self.write_csv(is_index=False, is_header=False)
        pass

def main():
    csv_handler = CSVHandler(r"")
    csv_handler.parse()
    pass


if __name__ == '__main__':
    main()