from loguru import logger


# record["extra"]：extra 是 Loguru 日志记录中一个特定的字段，用于存储附加信息。在例子的日志中使用了 logger.bind(module="module1")，这会将 module 字段添加到日志记录的 extra 字段中。
class Module1:
    def __init__(self):
        # 添加一个logger只用来记录module为module1的日志
        logger.add("./logs/module1.log", rotation="1 MB", retention="7 days", filter=lambda record: record["extra"].get("module") == "module1", mode="w")
        self.test_list = ["小明", "小红"]
        for name in self.test_list:
            name_log_path = f"./logs/{name}.log"
            # 添加logger以记录每个name的日志，其中name=name是为了修复可能导致错误的 lambda 闭包问题。
            logger.add(name_log_path, rotation="1 MB", retention="7 days", filter=lambda record, name=name: record["extra"].get("name") == name, mode="w")

    def func1(self):
        logger.bind(module="module1").info("module1的打印")

    def func2(self):
        for name in self.test_list:
            logger.bind(module="module1").info(f"{name}的打印")     # 打印到module1.log中
            logger.bind(name=name).info(f"{name}的打印")            # 打印到自己的名字中
            # 上面这行其实等于下面这两行，bind方法返回一个新的 logger 对象，该对象会自动将指定的上下文信息附加到日志消息中。
            # user_logger = logger.bind(name=name)
            # user_logger.info(f"{name}的打印")