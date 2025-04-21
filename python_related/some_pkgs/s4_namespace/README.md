# namespace命名空间

可以用命名空间模拟一些嵌套的变量，命名空间跟字典互转

`./namespace_utiles.py`中包含了几个函数：

- dict_to_namespace：将字典转成命名空间
- namespace_to_dict：将命名空间转成字典
- pretty_print_namespace：打印命名空间
- load_json：读取json文件，构建namespace
- load_yaml：读取yaml文件，构建namespace
- save_to_json：将命名空间保存成json

**字典转成命名空间**

```python
def dict_to_namespace(d):
    """
    递归地将 dict 转换为 SimpleNamespace。
    支持嵌套 dict 与 list。
    """
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_namespace(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [dict_to_namespace(item) for item in d]
    else:
        return d
```

**命名空间转成字典**

```python
def namespace_to_dict(ns):
    """
    递归地将 SimpleNamespace（或包含它的 list）转换回 dict。
    """
    if isinstance(ns, SimpleNamespace):
        return {k: namespace_to_dict(v) for k, v in vars(ns).items()}
    elif isinstance(ns, list):
        return [namespace_to_dict(item) for item in ns]
    else:
        return ns
```