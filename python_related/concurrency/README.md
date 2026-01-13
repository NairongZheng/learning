- [Python 并发编程教学](#python-并发编程教学)
  - [目录结构](#目录结构)
  - [如何判断任务类型](#如何判断任务类型)
    - [CPU密集型任务（CPU-bound）](#cpu密集型任务cpu-bound)
    - [I/O密集型任务（I/O-bound）](#io密集型任务io-bound)
  - [如何选择并发实现方式](#如何选择并发实现方式)
    - [决策流程图](#决策流程图)
    - [详细对比](#详细对比)
  - [代码示例](#代码示例)
    - [多进程（multiprocessing）](#多进程multiprocessing)
    - [多线程（threading）](#多线程threading)
    - [多协程（asyncio）](#多协程asyncio)
    - [混合并发（进程池 + 线程池）](#混合并发进程池--线程池)
  - [Python GIL（全局解释器锁）说明](#python-gil全局解释器锁说明)
  - [性能优化建议](#性能优化建议)
  - [参考资源](#参考资源)


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

## 代码示例

### 多进程（multiprocessing）

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count

def cpu_task(data):
    # CPU密集型任务
    return sum(i**2 for i in range(data))

# 方式1：使用 map（简单直接）
tasks = [10000, 20000, 30000]
with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
    futures = {executor.submit(cpu_task, task): task for task in tasks}
    results = []
    for future in as_completed(futures):
        results.append(future.result())
```

### 多线程（threading）

```python
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def io_task(url):
    # I/O密集型任务（如网络请求）
    time.sleep(0.1)  # 模拟I/O等待
    return f"Result from {url}"

# 使用线程池
urls = ["url1", "url2", "url3"]
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(io_task, url): url for url in urls}
    results = []
    for future in as_completed(futures):
        results.append(future.result())
```

### 多协程（asyncio）

```python
import asyncio

async def async_io_task(url):
    # 异步I/O任务
    await asyncio.sleep(0.1)  # 模拟I/O等待
    return f"Result from {url}"

# 并发执行协程
urls = ["url1", "url2", "url3"]
tasks = [async_io_task(url) for url in urls]
results = await asyncio.gather(*tasks)
```

### 混合并发（进程池 + 线程池）

```python
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from multiprocessing import cpu_count

def io_task(item):
    # I/O密集型任务
    time.sleep(0.1)
    return f"Processed {item}"

def process_batch(batch):
    # 在进程中使用线程池
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(io_task, batch))
    return results

# 使用进程池处理不同批次
batches = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
    results = list(executor.map(process_batch, batches))
```

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

- [Python官方文档 - threading](https://docs.python.org/zh-cn/3/library/threading.html)
- [Python官方文档 - multiprocessing](https://docs.python.org/zh-cn/3/library/multiprocessing.html)
- [Python官方文档 - asyncio](https://docs.python.org/zh-cn/3/library/asyncio.html)

