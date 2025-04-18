class MyObject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # 用户友好的字符串表示，用于print()或str()调用
        return f"MyObject: {self.name}"

    def __repr__(self):
        # 开发者友好的字符串表示，用于调试和repr()调用
        return f"MyObject(name='{self.name}')"


# 使用示例
obj = MyObject("TestObject")
print(str(obj))  # 输出: MyObject: TestObject
print(repr(obj))  # 输出: MyObject(name='TestObject')

print(obj)  # 如果没有指定str，会调用repr，这里调用__str__，输出: MyObject: TestObject
print([obj])  # 列表中的对象调用repr，输出: [MyObject(name='TestObject')]
