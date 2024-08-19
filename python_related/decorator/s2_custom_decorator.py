"""
只是提供一个示例, 正常人不会这么用
"""
from functools import wraps

# 不接受参数
def decorator_factory(func):
    @wraps(func)  # 也是一个装饰器, 通常用于在定义装饰器时, 保留被装饰函数的元数据, 包括函数名、文档字符串、参数签名等信息。
    def decorator(*args, **kwargs):
        print(f"\033[33mcall {func.__name__} without decorator para\033[0m")
        result = func(*args, **kwargs)  # 原函数(被装饰函数)
        if type(result) is list:
            return sum(result)
        elif type(result) is str:
            return result.upper()
        else:
            return result
    return decorator

# 接受参数(用这个)
def custom_decorator(action):
    # 外层: 装饰器工厂函数, 接收参数, 装饰器工厂函数允许传递参数来配置生成的装饰器
    def decorator_factory(func):
        # 中层: 接收一个func作为参数, func就是被装饰的函数
        @wraps(func)  # 也是一个装饰器, 通常用于在定义装饰器时, 保留被装饰函数的元数据, 包括函数名、文档字符串、参数签名等信息。
        def decorator(*args, **kwargs):
            # 内层: 真正的装饰器, 实际执行的功能
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


@decorator_factory()
def get_numbers1(number_list=[1, 2, 3, 4, 5]):
    return number_list


@decorator_factory
def get_string1(attr="hello world"):
    return attr

@decorator_factory
def get_none1():
    return "none"


@custom_decorator(action="sum")
def get_numbers2(number_list=[1, 2, 3, 4, 5]):
    return number_list


@custom_decorator(action="upper")
def get_string2(attr="hello world"):
    return attr

@custom_decorator(action="none")
def get_none2():
    return "none"


def main():
    # Testing the functions
    print(f"debug damonzheng, 测试一：不接受参数")
    print(get_numbers1())
    print(get_string1())
    print(get_none1())
    print(f"debug damonzheng, 测试二：接受参数")
    print(get_numbers2())
    print(get_string2())
    print(get_none2())


if __name__ == "__main__":
    main()
