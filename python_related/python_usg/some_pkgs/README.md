# some_pkgs一些包的用法

1. s1_enum.py：枚举
2. s2_dataclass.py：数据类(装饰器实现)
3. s3_pydantic.py：数据验证和设置管理库
4. s4_namespace.py：命名空间
5. s5_pandas.py：pandas
6. s6_logging：日志库logging的使用
7. s7_loguru：日志库loguru的使用
8. s8_asyncio：协程


## pandas
1. `pd.read_csv`：读取csv为df
2. `df.sample`：打乱
3. `pd.concat`：拼接
4. `df.sort_index`：用index排序
5. `df.reset_index`：重新编号
6. `df.drop`：删除行或列
7. `df.groupby`：分组

## loguru
1. `logger.add`：添加新的日志处理器，可以将日志输出到不同的目的地，如文件、控制台、网络等，并配置其行为。一些参数如下：
   1. `sink`（必需）：指定日志的输出目标，例如，`"./logs/my_log.log"`将日志写入文件，`sys.stdout`将日志输出到控制台。
   2. `level`（可选）：指定要记录的最低日志级别，常用的级别有 `DEBUG, INFO, WARNING, ERROR, CRITICAL`。只记录该级别及以上的日志。
   3. `format`（可选）：自定义日志消息的格式，例如，`"{time} {level} {message}"` 可以指定日志中显示时间、级别和消息。
   4. `rotation`（可选）：指定日志文件的轮换策略。可以是时间（如 `"1 day"`）或文件大小（如 `"1 MB"`）。当日志达到指定条件时，会自动创建新的日志文件。
   5. `retention`（可选）：指定日志文件的保留策略。可以是时间（如 `"10 days"`）或文件数量（如 `5`）。超过这个限制的旧日志将被删除。
   6. `filter`（可选）：一个函数或字典，用于过滤哪些日志记录应该被处理。该过滤器接收一个 `record` 字典，返回布尔值。例如，`filter=lambda record: record["level"].name == "ERROR"` 只记录错误日志。
   7. `mode`（可选）：指定打开日志文件的模式，常用的有 `"w"`（写入，覆盖）和 `"a"`（追加）。
   8. `catch`（可选）：布尔值，指示是否捕获在日志记录时发生的异常。
2. `logger.bind`：返回一个新的 logger 对象，**该对象会自动将指定的上下文信息附加到日志消息中**。可以配合`logger.add`中的`filter`使用