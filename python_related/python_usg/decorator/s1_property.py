class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

def main():
    circle = Circle(3)
    print(f"init radius is: {circle.radius}") # 直接访问方法获得属性
    circle.radius = 4 # 可以直接setter新的值
    print(f"new radius is: {circle.radius}")
    print(f"area is: {circle.area}") # 直接访问方法获得计算结果
    pass

if __name__ == "__main__":
    main()

# 与直接修改实例属性相比的好处：

# 1. 封装和数据隐藏：隐藏类的内部实现细节，对外提供统一的接口。这样，即使将来改变了内部实现，对外的接口也可以保持不变，从而提高了代码的可维护性。
# 2. 可以在属性设置时添加验证逻辑，确保数据的一致性和有效性。这在直接访问实例变量时是无法实现的。（比如本来一个属性的类型是str，但是直接给属性赋值可能就会改变他的类型，而使用property配合setter就可以加上验证逻辑来抛出错误）
# 3. 延迟计算属性：可以在访问属性时执行计算，将计算结果作为属性值返回。这在直接访问实例变量时也是无法实现的。
# 4. 只读和只写属性：可以创建只读属性（没有 setter）和只写属性（没有 getter），以限制属性的访问权限。（比如在setter的时候，检测如果已经有值了，再setter就抛出错误）
# 5. 统一接口：允许你将方法和属性统一在一起，提供一个统一的接口。这样可以避免破坏已有的代码。