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
        variables.general_vars.type = "class2namespace"
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
            "type": "dict2namespace",
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


def class2namespace():
    fake_vars = FakeVars()
    variables = fake_vars.set_vars()
    return variables


def json2namespace():
    json_file_path = "python_related/some_pkgs/s4_namespace/tmp_files/json2namespace.json"
    variables = NamespaceUtils.load_json(json_file_path)
    return variables


def yaml2namespace():
    yaml_file_path = "python_related/some_pkgs/s4_namespace/tmp_files/yaml2namespace.yaml"
    variables = NamespaceUtils.load_yaml(yaml_file_path)
    return variables


def namespace2json(ns):
    save_file_path = "python_related/some_pkgs/s4_namespace/tmp_files/namespace2json.json"
    NamespaceUtils.save_to_json(ns, save_file_path)


def main():
    # 1. 用类构建namespace（较麻烦）
    print(f" ==================== class to namespace ==================== ")
    variables_1_namespace = class2namespace()
    print(f"class2namespace: {variables_1_namespace}\n")
    
    # 2. 用字典构建namespace（方便点）
    print(f" ==================== dict to namespace ==================== ")
    variables_2_namespace = dict2namespace()
    print(f"dict2namespace: {variables_2_namespace}\n")
    
    # 3. 用json构建namespace（JSON 只支持基础数据类型）
    print(f" ==================== json to namespace ==================== ")
    variables_3_namespace = json2namespace()
    print(f"json2namespace: {variables_3_namespace}\n")
    
    # 4. 用yaml构建namespace
    print(f" ==================== yaml to namespace ==================== ")
    variables_4_namespace = yaml2namespace()
    print(f"json2namespace: {variables_4_namespace}\n")
    
    # 5. namespace保存到json
    print(f" ==================== namespace to json ==================== ")
    namespace2json(variables_2_namespace)
    print(f"save success")


if __name__ == "__main__":
    main()
