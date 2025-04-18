from dataclasses import dataclass, field
from typing import List


@dataclass
class Person:
    """
    name: 普通字段，必须在初始化时传入。
    age: 具有默认值 30，如果在创建对象时没有传递 age 参数，默认值会生效。
    hobbies: 使用 default_factory 来生成一个空列表作为默认值。这样避免了在类级别共享可变对象（如列表）的潜在问题。
    secret: 使用 repr=False，该字段不会包含在生成的 __repr__ 方法中。
    id: 使用 init=False，意味着它不会出现在 __init__ 方法的参数列表中，但是可以有默认值，后续可以手动赋值。
    """
    name: str  # 普通字段
    age: int = 30  # 默认值
    hobbies: List[str] = field(default_factory=list)  # 使用default_factory生成默认值，当使用 default=[] 时，所有实例的 hobbies 字段都会共享同一个列表。
    secret: str = field(default="", repr=False)  # 不在repr中显示
    id: int = field(default=0, init=False)  # 不会作为__init__的参数


person = Person(name="Alice", secret="my_secret")
print(person)  # Person(name='Alice', age=30, hobbies=[], id=0), 输出中不显示 secret 字段
