# python使用

1. decorator：装饰器
2. magic_fun：魔术方法
3. some_pkgs：一些包的用法


## super继承
1. 基本用法
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的 __init__ 方法
        self.breed = breed

    def speak(self):
        super().speak()  # 调用父类的 speak 方法
        print("Dog barks")
```

2. 多重继承
```python
# 多重继承mro
class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        super().method()
        print("Method in B")

class C(A):
    def method(self):
        super().method()
        print("Method in C")

class D(B, C):
    def method(self):
        super().method()
        print("Method in D")

if __name__ == '__main__:
    d = D()
    d.method()

    # # 输出
    # Method in A
    # Method in C
    # Method in B
    # Method in D
```