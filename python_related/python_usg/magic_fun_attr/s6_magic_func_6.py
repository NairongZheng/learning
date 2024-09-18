class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        # 使对象可调用（直接加括号传参可用，不需要调用类里方法）
        return self.factor * value


# 使用示例
times_two = Multiplier(2)
print(times_two(5))  # 输出: 10

times_three = Multiplier(3)
print(times_three(5))  # 输出: 15
