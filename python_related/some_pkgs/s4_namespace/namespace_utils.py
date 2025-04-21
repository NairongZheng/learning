from typing import Any, Dict, Union
import json, yaml, datetime, decimal
from types import SimpleNamespace


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
    
    @staticmethod
    def load_json(file_path: str, verbose: bool = False) -> SimpleNamespace:
        """
        读取json文件，构建namespace
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return NamespaceUtils.build_namespace(data, verbose)

    @staticmethod
    def load_yaml(file_path: str, verbose: bool = False) -> SimpleNamespace:
        """
        读取yaml文件，构建namespace
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return NamespaceUtils.build_namespace(data, verbose)

    @staticmethod
    def save_to_json(ns: SimpleNamespace, file_path: str) -> None:
        """
        将命名空间保存成json（支持函数转为字符串）
        """
        dict_data = NamespaceUtils.namespace_to_dict(ns)
        
        # def fallback(obj):
        #     if callable(obj):
        #         return f"<function:{obj.__name__}>"
        #     return str(obj)  # fallback for other non-serializable types

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, indent=4, ensure_ascii=False, default=NamespaceUtils.safe_json_default)
    
    @staticmethod
    def safe_json_default(obj):
        """
        通用 fallback，用于 json.dump 的 default 参数。
        将不可序列化的对象转为可读字符串。
        """
        if callable(obj):
            return f"<function:{obj.__name__}>"
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif hasattr(obj, '__dict__'):
            return {k: NamespaceUtils.safe_json_default(v) for k, v in vars(obj).items()}
        return str(obj)  # 最终兜底
