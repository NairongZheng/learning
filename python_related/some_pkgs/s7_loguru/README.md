# loguru日志库

Loguru是一个强大且易用的Python日志库，相比标准库的logging更加简洁和强大。

## 为什么选择loguru

1. **开箱即用**：无需复杂配置，直接使用即可
2. **自动格式化**：自动彩色输出，更易读
3. **异常追踪**：更好的异常信息展示
4. **文件轮转**：内置日志文件轮转功能
5. **简洁API**：比标准库logging更简单

## 核心功能

### 1. 基本使用
```python
from loguru import logger

logger.debug("这是一条调试信息")
logger.info("这是一条普通信息")
logger.warning("这是一条警告信息")
logger.error("这是一条错误信息")
logger.critical("这是一条严重错误信息")
```

### 2. logger.add() - 添加日志处理器

`logger.add`用于添加新的日志处理器，可以将日志输出到不同的目的地。

#### 主要参数

1. **sink**（必需）：指定日志的输出目标
   - 文件路径：`"./logs/my_log.log"`
   - 控制台：`sys.stdout`
   - 自定义函数：接收日志消息的函数

2. **level**（可选）：指定要记录的最低日志级别
   - 常用级别：`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
   - 只记录该级别及以上的日志

3. **format**（可选）：自定义日志消息的格式
   ```python
   format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
   ```

4. **rotation**（可选）：指定日志文件的轮换策略
   - 按时间：`"1 day"`, `"1 week"`, `"00:00"`（每天午夜）
   - 按大小：`"1 MB"`, `"500 KB"`
   - 自动创建新文件

5. **retention**（可选）：指定日志文件的保留策略
   - 按时间：`"10 days"`（保留10天）
   - 按数量：`5`（保留5个文件）
   - 超过限制的旧日志将被删除

6. **compression**（可选）：日志文件压缩格式
   - 支持：`"zip"`, `"gz"`, `"bz2"`, `"xz"`

7. **filter**（可选）：过滤日志记录
   - 函数或字典，用于过滤哪些日志应该被处理
   - 示例：`filter=lambda record: record["level"].name == "ERROR"`

8. **mode**（可选）：打开日志文件的模式
   - `"w"`：写入（覆盖）
   - `"a"`：追加（默认）

9. **catch**（可选）：是否捕获日志记录时的异常
   - 布尔值，默认为True

#### 使用示例

```python
from loguru import logger

# 基本文件输出
logger.add("app.log", level="INFO")

# 带轮转的文件输出
logger.add(
    "logs/app_{time}.log",
    rotation="1 day",      # 每天轮换
    retention="7 days",    # 保留7天
    compression="zip",     # 压缩旧日志
    level="DEBUG"
)

# 按大小轮转
logger.add(
    "logs/app.log",
    rotation="10 MB",      # 每10MB轮换
    level="INFO"
)

# 自定义格式
logger.add(
    "logs/custom.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {message}",
    level="WARNING"
)
```

### 3. logger.bind() - 绑定上下文信息

`logger.bind`返回一个新的logger对象，该对象会自动将指定的上下文信息附加到日志消息中。

```python
# 绑定用户信息
user_logger = logger.bind(user_id=123, username="Alice")
user_logger.info("用户登录")  # 自动包含user_id和username

# 结合filter使用
logger.add(
    "users.log",
    filter=lambda record: "user_id" in record["extra"]
)
```

### 4. 异常捕获

```python
@logger.catch
def my_function():
    # 函数中的异常会被自动记录
    raise ValueError("出错了")

# 或者使用上下文管理器
with logger.catch():
    # 代码块中的异常会被记录
    1 / 0
```

### 5. 序列化

```python
# 输出JSON格式的日志
logger.add("logs/json.log", serialize=True)
```

## 示例文件说明

- **s7_1_main.py**: loguru的基本使用和配置示例
- **s7_2_module1.py**: 在模块中使用loguru

## 与logging对比

| 特性 | logging | loguru |
|------|---------|--------|
| 配置复杂度 | 需要配置Handler、Formatter等 | 开箱即用，简单配置 |
| 彩色输出 | 需要第三方库 | 内置支持 |
| 文件轮转 | 需要RotatingFileHandler | 一个参数搞定 |
| 异常追踪 | 基本 | 更详细美观 |
| 性能 | 较好 | 稍慢，但可接受 |

## 最佳实践

1. **生产环境配置**
```python
logger.remove()  # 移除默认处理器
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)
logger.add(
    "logs/app_{time}.log",
    rotation="00:00",
    retention="30 days",
    compression="zip",
    level="DEBUG"
)
```

2. **错误日志单独记录**
```python
logger.add(
    "logs/error_{time}.log",
    rotation="1 day",
    level="ERROR",
    backtrace=True,
    diagnose=True
)
```

## 参考资源

- [Loguru官方文档](https://loguru.readthedocs.io/)
- [GitHub仓库](https://github.com/Delgan/loguru)
