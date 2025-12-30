# Python相关学习资源

本目录包含Python编程相关的学习代码和示例，涵盖多线程、网络通信、装饰器、魔术方法、PyQt GUI编程以及常用Python包的使用。

## 目录结构

### 1. [connection](./connection/) - 网络通信
各种通信协议的Python实现案例，包括：
- **tcp_and_udp**: 基础的TCP/UDP传输
- **tcp_file**: 使用读写方法进行数据传输（TCP + Protobuf）
- **tcp_stream**: 使用流式方法进行数据传输（TCP + Protobuf）
- **http_connect**: HTTP通信（Tornado、FastAPI框架）
- **grpc_connect**: gRPC通信（Protobuf，多进程非阻塞）
- **grpc_connect2**: gRPC通信（Protobuf，多进程阻塞）

### 2. [threading](./threading/) - 多线程与并发
Python并发编程实战，包括多线程、多进程、协程等：
- 线程池的使用
- 生产者-消费者模式
- 锁与并发控制
- Flask线程池和进程池
- 异步爬虫示例

### 3. [decorator](./decorator/) - 装饰器
装饰器的各种使用场景：
- `@property`装饰器
- 自定义装饰器
- 类注册器模式

### 4. [magic_fun_attr](./magic_fun_attr/) - 魔术方法与魔术属性
Python的特殊方法和属性：
- **魔术方法**: `__init__`, `__str__`, `__repr__`, `__add__`, `__getattr__`, `__setattr__`, `__enter__`, `__exit__`, `__call__`等
- **魔术属性**: `__dict__`, `__class__`, `__bases__`, `__mro__`, `__slots__`, `__doc__`等

### 5. [pyqt](./pyqt/) - PyQt GUI编程
基于PyQt6/PySide2的桌面应用开发：
- PyQt入门示例
- 密码生成器小程序
- JSON格式化工具

### 6. [some_pkgs](./some_pkgs/) - Python常用包
常用Python包和标准库的使用示例：

#### 数据处理
- **s1_enum.py**: 枚举类型
- **s2_dataclass.py**: 数据类（装饰器实现）
- **s3_pydantic.py**: 数据验证和设置管理
- **s4_namespace**: 命名空间操作
- **s5_pandas.py**: Pandas数据分析

#### 日志系统
- **s6_logging**: 标准库logging的使用
- **s7_loguru**: Loguru日志库（推荐）

#### 异步编程
- **s8_asyncio**: 协程与异步编程

#### 网络爬虫
- **s9_bs**: BeautifulSoup爬虫示例

#### 机器学习
- **s10_scikit-learn**: Scikit-learn机器学习

#### 文本与图像处理
- **s11_re.py**: 正则表达式
- **s12_PIL.py**: PIL图像处理
- **s13_cv2.py**: OpenCV图像处理

#### Web框架
- **s14_fastapi**: FastAPI Web框架

#### 工具类
- **s15_argparse.py**: 命令行参数解析
- **s16_tempfile.py**: 临时文件处理
- **s17_requests.py**: HTTP请求库
- **s18_pathlib.py**: 现代路径处理
- **s19_json.py**: JSON操作
- **s20_datetime.py**: 日期时间处理
- **s21_collections.py**: 特殊数据结构
- **s22_itertools.py**: 迭代器工具

## 学习建议

### 入门路径
1. 先学习基础的装饰器和魔术方法
2. 掌握常用包的使用（some_pkgs目录）
3. 学习多线程和并发编程
4. 深入网络通信和协议

### 进阶路径
1. 异步编程（asyncio）
2. 网络编程（socket、HTTP、gRPC）
3. GUI开发（PyQt）
4. Web开发（FastAPI）

## 相关资源

- [Python官方文档](https://docs.python.org/zh-cn/3/)
- [Real Python](https://realpython.com/)
- [Python并发编程视频教程](https://www.bilibili.com/video/BV1bK411A7tV)

## 贡献说明

所有代码都是参考网络资源学习整理而来，仅供学习参考。