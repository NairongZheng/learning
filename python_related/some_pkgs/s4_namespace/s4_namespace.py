from types import SimpleNamespace
from namespace_utils import NamespaceUtils


# functions
def greet(name):
    return f"Hello, {name}!"

def sum_numbers(a, b):
    return a + b


class FakeVars:
    def __init__(self):
        pass

    def set_vars(self):
        # variables
        variables = SimpleNamespace()
        variables.general_vars = SimpleNamespace()
        variables.people_related = SimpleNamespace()
        variables.functions = SimpleNamespace()
        # general_vars
        variables.general_vars.version = "1.1.1"
        variables.general_vars.date = "20240919"
        # people_related
        people_num = 2
        variables.people_related.people_num = people_num
        variables.people_related.people_name_list = [None for _ in range(people_num)]
        # functions
        variables.functions.greet = greet
        variables.functions.sum_numbers = sum_numbers
        return variables


def dict2namespace():
    people_num = 2
    variables = {
        "general_vars": {
            "version": "1.1.1",
            "date": "20250418"
        },
        "people_related": {
            "people_num": people_num,
            "people_name_list": [None for _ in range(people_num)]
        },
        "functions": {
            "greet": greet,
            "sum_numbers": sum_numbers
        }
    }
    adict_namespace = NamespaceUtils.build_namespace(variables) # 字典转化成命名空间
    return adict_namespace


def main():
    # 写类直接构建返回，比较麻烦
    fake_vars = FakeVars()
    variables_1_namespace = fake_vars.set_vars()
    print(variables_1_namespace)
    variables_1_dict = NamespaceUtils.namespace_to_dict(variables_1_namespace) # 命名空间转化成字典
    print(variables_1_dict)
    
    # 用字典自动转换，很方便
    variables_2_namespace = dict2namespace()
    # NamespaceUtils.pretty_print_namespace(variables_2_namespace)
    pass


if __name__ == "__main__":
    main()
