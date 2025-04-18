class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        # 定义 len()
        return len(self.data)

    def __getitem__(self, index):
        # 定义索引访问
        return self.data[index]

    def __setitem__(self, index, value):
        # 定义索引赋值
        self.data[index] = value

    def __delitem__(self, index):
        # 定义索引删除
        del self.data[index]

    def __iter__(self):
        # 定义迭代器
        return iter(self.data)

    def __contains__(self, item):
        # 定义 in 运算符
        return item in self.data


# 使用示例
my_list = MyList([1, 2, 3, 4])
print(len(my_list))  # 输出: 4
print(my_list[2])  # 输出: 3
my_list[2] = 10
print(my_list[2])  # 输出: 10
del my_list[2]
print(len(my_list))  # 输出: 3

for item in my_list:
    print(item)  # 输出: 1 2 4

print(2 in my_list)  # 输出: True
print(5 in my_list)  # 输出: False
