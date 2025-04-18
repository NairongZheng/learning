class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 控制对象的创建，实现单例模式
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

    def __del__(self):
        # 对象被销毁时调用
        print(f"对象 {self} 被销毁")


# 使用示例
s1 = Singleton(10)
s2 = Singleton(20)

print(s1.value)  # 输出: 20
print(s2.value)  # 输出: 20
print(s1 is s2)  # 输出: True

del s1
del s2
