class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # 定义加法运算符 +
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # 定义减法运算符 -
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        # 定义乘法运算符 *
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        # 定义相等运算符 ==
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# 使用示例
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)  # 输出: Vector(6, 8)
print(v1 - v2)  # 输出: Vector(-2, -2)
print(v1 * 3)  # 输出: Vector(6, 9)
print(v1 == v2)  # 输出: False
