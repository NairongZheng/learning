# __slots__ 魔术属性


class SlotClass:
    __slots__ = ["name", "age"]  # 限制实例只能有这两个属性

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.gender = 'M'     # 会报错


# 使用示例
slot_obj = SlotClass("Bob", 30)
print(slot_obj.name)  # 输出: Bob
# slot_obj.gender = 'M'  # 会引发 AttributeError: 'SlotClass' object has no attribute 'gender'
