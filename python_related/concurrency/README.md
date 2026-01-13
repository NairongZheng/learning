# Python 并发编程教学

本文件夹包含 Python 中多进程、多线程、多协程的教学示例和说明。

## 目录结构

- `backup/` - 原有 threading 文件夹的备份内容
- `01_multiprocessing.py` - 多进程示例（CPU密集型任务）
- `02_multithreading.py` - 多线程示例（I/O密集型任务）
- `03_asyncio.py` - 多协程示例（I/O密集型任务）
- `04_hybrid.py` - 混合使用示例（复杂场景）

## 如何判断任务类型

### CPU密集型任务（CPU-bound）
- **特点**：大量计算操作，CPU使用率高
- **示例**：
  - 数学计算（素数判断、矩阵运算）
  - 数据加密/解密
  - 图像/视频处理
  - 机器学习模型训练
  - 科学计算

### I/O密集型任务（I/O-bound）
- **特点**：大量等待外部资源（磁盘、网络、数据库）
- **示例**：
  - 网络请求（爬虫、API调用）
  - 文件读写操作
  - 数据库查询
  - 网络服务器处理请求

## 如何选择并发实现方式

### 决策流程图

```
任务类型判断
    │
    ├─→ CPU密集型任务
    │       │
    │       └─→ 使用多进程（multiprocessing）
    │           - 绕过GIL限制
    │           - 充分利用多核CPU
    │           - 示例：01_multiprocessing.py
    │
    └─→ I/O密集型任务
            │
            ├─→ 需要大量并发连接（1000+）
            │       │
            │       └─→ 使用协程（asyncio）
            │           - 单线程异步
            │           - 最高效的I/O处理
            │           - 示例：03_asyncio.py
            │
            └─→ 中等并发需求（<1000）
                    │
                    └─→ 使用多线程（threading）
                        - 编程简单直观
                        - 适合中等规模I/O
                        - 示例：02_multithreading.py
```

### 详细对比

| 特性 | 多进程 | 多线程 | 多协程 |
|------|--------|--------|--------|
| **适用场景** | CPU密集型 | I/O密集型 | 高并发I/O密集型 |
| **GIL影响** | 无（独立进程） | 有（受限于GIL） | 无（单线程） |
| **内存开销** | 大（独立内存空间） | 中（共享内存） | 小（单线程） |
| **启动开销** | 大 | 中 | 小 |
| **并发数量** | 受CPU核心限制 | 几十到几百 | 成千上万 |
| **编程复杂度** | 中 | 低 | 中高 |
| **数据共享** | 需要IPC机制 | 简单（但需加锁） | 简单（无需加锁） |
| **典型库** | multiprocessing | threading, concurrent.futures | asyncio, aiohttp |

## 实际应用场景举例

### 场景1：文件路径读取与JSON处理
**问题描述**：某文件中存放大量文件路径，需要读取每个文件、json.load解析、处理后保存。

**分析**：
- 读取文件：I/O操作
- json.load：CPU操作（较轻量）
- 保存文件：I/O操作

**推荐方案**：
1. **优先选择**：多线程（threading）- 平衡了I/O处理和编程复杂度
2. **高并发场景**：协程（asyncio + aiofiles）- 如果文件数量巨大（10000+）
3. **不推荐**：多进程 - I/O操作不受GIL影响，多进程开销大

参考代码：`04_hybrid.py` 中的文件处理示例

### 场景2：网络爬虫
**推荐**：协程（asyncio + aiohttp）
- 大量HTTP请求
- 网络等待时间长
- 协程可以实现高并发

参考代码：`03_asyncio.py`

### 场景3：图像批处理
**推荐**：多进程（multiprocessing）
- CPU密集的图像处理算法
- 充分利用多核CPU

参考代码：`01_multiprocessing.py`

### 场景4：Web服务器
**推荐**：混合模式
- 多进程：启动多个worker进程
- 每个进程内使用协程：处理大量并发请求

参考代码：`04_hybrid.py` 中的Web服务示例

## Python GIL（全局解释器锁）说明

**GIL是什么**：
- Global Interpreter Lock（全局解释器锁）
- CPython解释器的机制，同一时刻只允许一个线程执行Python字节码

**GIL的影响**：
- **多线程**：CPU密集型任务无法真正并行，受GIL限制
- **多进程**：每个进程有独立的GIL，可以真正并行
- **协程**：单线程异步，不受GIL影响（因为本来就是单线程）

## 性能优化建议

1. **先profile，后优化**：使用 `cProfile` 或 `line_profiler` 确定瓶颈
2. **选择合适的并发方式**：根据任务类型选择
3. **控制并发数量**：过多的线程/进程反而降低性能
4. **使用线程池/进程池**：避免频繁创建销毁的开销
5. **注意资源竞争**：使用锁（Lock）、队列（Queue）等同步机制

## 参考资源

- [Python并发编程实战](https://www.bilibili.com/video/BV1bK411A7tV)
- [Python官方文档 - threading](https://docs.python.org/zh-cn/3/library/threading.html)
- [Python官方文档 - multiprocessing](https://docs.python.org/zh-cn/3/library/multiprocessing.html)
- [Python官方文档 - asyncio](https://docs.python.org/zh-cn/3/library/asyncio.html)

## 快速开始

运行示例代码：
```bash
# 多进程示例
python 01_multiprocessing.py

# 多线程示例
python 02_multithreading.py

# 多协程示例
python 03_asyncio.py

# 混合示例
python 04_hybrid.py
```
