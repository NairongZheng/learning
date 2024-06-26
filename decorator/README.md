# decorator装饰器

- s1_property.py: 装饰器property使用例子
- s2_custom_decorator.py: 自定义装饰器例子([参考链接](https://www.cnblogs.com/serpent/p/9445592.html))
- s3_class_register.py: 类注册器例子([参考链接](https://zhuanlan.zhihu.com/p/350821621))
- (比较抽象, 调试着看看能看懂的, 下面有简单说明)

## 自定义装饰器例子
第一步：表示原来的函数
```python
result = func(*args, **kwargs) # result就是原来函数的返回值
```

第二步：添加装饰器要实现的功能
```python
def decorator_factory(func):
    @wraps(func)  # 也是一个装饰器, 通常用于在定义装饰器时, 保留被装饰函数的元数据, 包括函数名、文档字符串、参数签名等信息。
    def decorator(*args, **kwargs):
        # 在这里实现要加的功能
        result = func(*args, **kwargs)
        # 在这里实现要加的功能
    return decorator
```

第三步：若装饰器实现的功能需要传参，就再套一层用来传参
```python
def custom_decorator(action): # 最终写在函数上面那行的@后面的那个名字, 即装饰器最终的名字
    def decorator_factory(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            print(f"\033[33mcall {func.__name__} with action '{action}'\033[0m")
            result = func(*args, **kwargs)
            if action == "sum":
                return sum(result)
            elif action == "upper":
                return result.upper()
            else:
                return result
        return decorator
    return decorator_factory
```