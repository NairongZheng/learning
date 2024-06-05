"""
只是提供一个示例, 正常人不会这么用
"""
from functools import wraps


def custom_decorator(action):  # 外层: 装饰器工厂函数, 接收参数, 装饰器工厂函数允许传递参数来配置生成的装饰器
    def decorator_factory(func):  # 中层: 接收一个func作为参数, func就是被装饰的函数
        @wraps(func)  # 也是一个装饰器, 通常用于在定义装饰器时, 保留被装饰函数的元数据, 包括函数名、文档字符串、参数签名等信息。
        def decorator(*args, **kwargs):  # 内层: 真正的装饰器, 实际执行的功能
            print(f"\033[33mcall {func.__name__} with action '{action}'\033[0m")
            result = func(*args, **kwargs)  # 原函数(被装饰函数)
            if action == "sum":
                return sum(result)
            elif action == "upper":
                return result.upper()
            else:
                return result

        return decorator

    return decorator_factory


@custom_decorator(action="sum")
def get_numbers():
    return [1, 2, 3, 4, 5]


@custom_decorator(action="upper")
def get_string():
    return "hello world"


def main():
    # Testing the functions
    print(get_numbers())
    print(get_string())


if __name__ == "__main__":
    main()
