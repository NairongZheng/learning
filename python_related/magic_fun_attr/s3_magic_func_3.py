class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        # 当访问不存在的属性时调用
        return f"没有属性 {attr}"
    
    # def __getattribute__(self, name):
    #     """
    #     访问任何属性时调用
    #     用于对属性访问进行全局拦截和处理。它适用于需要监控或修改每个属性访问的场景。
    #     调用频率高，因为它在每次访问属性时都会被调用。如果不小心实现，可能会导致性能问题。
    #     """
    #     print(f"访问属性 {name}")
    #     return super().__getattribute__(name)

    def __setattr__(self, name, value):
        # 设置属性时调用
        print(f"设置属性 {name} 为 {value}")
        # 为避免无限递归，使用super().__setattr__()
        super().__setattr__(name, value)

    def __delattr__(self, name):
        # 删除属性时调用
        print(f"删除属性 {name}")
        super().__delattr__(name)


# 使用示例
p = Person("Alice")
print(p.name)  # 输出: Alice
print(p.age)  # 输出: 没有属性 age
p.age = 30  # 输出: 设置属性 age 为 30
print(p.age)  # 输出: 30
del p.age  # 输出: 删除属性 age
pass