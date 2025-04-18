from types import SimpleNamespace
from typing import Any, Dict, Union


class NamespaceUtils:
    @staticmethod
    def dict_to_namespace(d: Any) -> Any:
        """
        递归地将 dict 转换为 SimpleNamespace。
        支持嵌套 dict 与 list。
        """
        if isinstance(d, dict):
            return SimpleNamespace(**{k: NamespaceUtils.dict_to_namespace(v) for k, v in d.items()})
        elif isinstance(d, list):
            return [NamespaceUtils.dict_to_namespace(item) for item in d]
        else:
            return d

    @staticmethod
    def namespace_to_dict(ns: Any) -> Any:
        """
        递归地将 SimpleNamespace（或包含它的 list）转换回 dict。
        """
        if isinstance(ns, SimpleNamespace):
            return {k: NamespaceUtils.namespace_to_dict(v) for k, v in vars(ns).items()}
        elif isinstance(ns, list):
            return [NamespaceUtils.namespace_to_dict(item) for item in ns]
        else:
            return ns

    @staticmethod
    def build_namespace(mock_dict: Dict[str, Any], verbose: bool = False) -> SimpleNamespace:
        """
        构建 namespace，可选打印结构。
        """
        namespace = NamespaceUtils.dict_to_namespace(mock_dict)
        if verbose:
            print("[NamespaceUtils] 构建完成的命名空间结构如下：")
            NamespaceUtils.pretty_print_namespace(namespace)
        return namespace

    @staticmethod
    def pretty_print_namespace(ns: Union[SimpleNamespace, Any], indent: int = 0) -> None:
        """
        格式化打印 namespace 的内容（递归结构）。
        """
        prefix = '  ' * indent
        if isinstance(ns, SimpleNamespace):
            for key, value in ns.__dict__.items():
                if isinstance(value, SimpleNamespace):
                    print(f"{prefix}{key}:")
                    NamespaceUtils.pretty_print_namespace(value, indent + 1)
                elif isinstance(value, list):
                    print(f"{prefix}{key}: [")
                    for idx, item in enumerate(value):
                        print(f"{prefix}  [{idx}]:")
                        NamespaceUtils.pretty_print_namespace(item, indent + 2)
                    print(f"{prefix}]")
                else:
                    print(f"{prefix}{key}: {value}")
        else:
            print(f"{prefix}{ns}")
