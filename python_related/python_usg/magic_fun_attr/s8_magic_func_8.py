"""
来自gpt：

描述器的好处
封装属性管理逻辑：描述器允许你将属性的获取、设置和删除逻辑封装到一个独立的类中，使得这些逻辑不会分散到多个类中，从而提高代码的可维护性。
重用逻辑：你可以将描述器应用于多个类或多个属性，使得相同的属性管理逻辑可以在不同的类中重用，而无需重复编写相同的代码。
简化类定义：使用描述器可以减少类中的代码量，使得类的定义更加简洁。你可以将复杂的属性逻辑从类中抽离出来，保持类的核心功能简单明了。

总结
使用描述器可以将属性的管理逻辑集中在一个地方，使得代码更模块化和可重用。即使最初看起来有些抽象，描述器的使用可以显著提高代码的组织性和维护性。通过具体的例子，你可以看到描述器如何使属性管理变得更加灵活和安全。
"""
class PositiveNumber:
    """定义了一个描述器"""
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        # 获取属性值
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # 设置属性值，并进行验证
        if value < 0:
            raise ValueError("值必须为非负数")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        # 删除属性值
        del instance.__dict__[self.name]

class Account:
    balance = PositiveNumber("balance") # Account 类定义了一个属性 balance，它是 PositiveNumber 的实例，因此 balance 成为一个描述器属性。

    def __init__(self, initial_balance):
        self.balance = initial_balance # 由于 balance 是一个描述器，调用 self.balance = initial_balance 时会触发 PositiveNumber.__set__ 方法，将初始余额存储到实例的属性字典中。

# 使用示例
account = Account(100)
print(account.balance)    # 输出: 100
account.balance = 200
print(account.balance)    # 输出: 200
# account.balance = -50    # 会引发 ValueError: 值必须为非负数
del account.balance
# print(account.balance)  # 会引发 AttributeError