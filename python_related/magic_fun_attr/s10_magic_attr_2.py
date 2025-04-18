"""
__dict__：
    作用：这是一个标准属性，存储对象的属性字典。对于自定义对象，它包含实例的属性及其值。
    使用场景：可以查看或修改对象的属性字典，通常用于调试或动态操作对象属性。
__class__：
    作用：这是一个标准属性，指向对象的类。用于动态获取对象的类信息。
    使用场景：可以用来动态检查或操作对象的类。
__bases__：
    作用：这是一个元类属性，返回一个元组，包含类的基类。用于动态获取类的继承信息。
    使用场景：可以用来查看或操作类的继承结构。
__mro__：
    作用：这是一个元组，表示类的继承顺序（方法解析顺序）。从对象本身开始，依次列出类及其基类。
    使用场景：可以用来查看类的继承顺序，帮助理解多重继承的复杂性。
__doc__：
    作用：这是一个标准属性，包含类或函数的文档字符串（docstring）。用于生成文档和帮助信息。
    使用场景：可以用来获取类或函数的文档字符串，用于帮助信息或文档生成工具。
"""

class Creature:
    """这是一个Creature类"""
    pass


class Person(Creature):
    """这是一个Person类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Man(Person):
    def __init__(self, name, age):
        """这是Man的构造函数"""
        super(Man, self).__init__(name, age)    # super(Man, self)：super 函数的第一个参数是当前类（Man），第二个参数是当前实例（self）。这告诉 super 对象应该从哪个类开始查找父类方法。
        # super().__init__(name, age)    # python3中的简洁写法
        pass


def main():
    a_man = Man("damon", 27)
    # __dict__
    print(a_man.__dict__)   # {'name': 'damon', 'age': 27}
    # __class__
    print(a_man.__class__)  # <class '__main__.Man'>
    # __bases__
    print(Person.__base__)  # <class '__main__.Creature'>
    print(Man.__base__)     # <class '__main__.Person'>
    # __mro__
    print(Man.__mro__)      # (<class '__main__.Man'>, <class '__main__.Person'>, <class '__main__.Creature'>, <class 'object'>)
    # __doc__
    print(Creature.__doc__)          # 这是一个Creature类
    print(Person.__doc__)            # 这是一个Person类
    print(Man.__doc__)               # None（因为没写）
    print(Man.__init__.__doc__)      # 这是Man的构造函数
    pass


if __name__ == '__main__':
    main()