
from typing import Any, Dict, Union
from types import SimpleNamespace


def dict_to_namespace(d: Any) -> Any:
    """
    递归地将 dict 转换为 SimpleNamespace。
    支持嵌套 dict 与列表。
    """
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_namespace(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [dict_to_namespace(item) for item in d]
    else:
        return d


def build_namespace(mock_dict: Dict[str, Any], verbose: bool = False) -> SimpleNamespace:
    """
    构建 namespace，可选打印结构。
    
    :param mock_dict: 输入的嵌套字典
    :param verbose: 是否打印构造结果
    :return: 构建后的 SimpleNamespace
    """
    namespace = dict_to_namespace(mock_dict)
    if verbose:
        print("[build_namespace] 构建完成的命名空间结构如下：")
        pretty_print_namespace(namespace)
    return namespace


def pretty_print_namespace(ns: Union[SimpleNamespace, Any], indent: int = 0) -> None:
    """
    格式化打印 namespace 的内容（递归结构）。
    """
    prefix = '  ' * indent
    if isinstance(ns, SimpleNamespace):
        for key, value in ns.__dict__.items():
            if isinstance(value, SimpleNamespace):
                print(f"{prefix}{key}:")
                pretty_print_namespace(value, indent + 1)
            elif isinstance(value, list):
                print(f"{prefix}{key}: [")
                for idx, item in enumerate(value):
                    print(f"{prefix}  [{idx}]:")
                    pretty_print_namespace(item, indent + 2)
                print(f"{prefix}]")
            else:
                print(f"{prefix}{key}: {value}")
    else:
        print(f"{prefix}{ns}")