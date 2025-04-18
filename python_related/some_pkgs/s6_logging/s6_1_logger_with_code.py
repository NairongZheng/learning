"""
直接代码定义logger
"""
import logging
import time
import os


class Logger:
    def __init__(self):
        self.reset()

    def reset(self):
        cur_dir_path = os.path.dirname(os.path.abspath(__file__))
        self.log_path = os.path.join(cur_dir_path, "logs")

    def create_logger(self):
        # 1. 记录器logger(笔)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)  # logger默认优先, 指定最低级DEBUG, 方便后面设置的handler的级别

        # 2. 处理器handler(写到哪里)
        # 写到console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        # 写到文件
        # FileHandler: 普通日志文件
        # RotatingFileHandler: 根据文件大小轮换日志
        # TimedRotatingFileHandler: 根据时间轮换日志
        time_str = time.strftime("%Y-%m-%d-%H-%M")
        log_file_path = os.path.join(self.log_path, f"{time_str}.log")
        file_handler = logging.FileHandler(filename=log_file_path, encoding="utf-8", mode="w")
        file_handler.setLevel(logging.INFO)

        # 3. 格式器formatter
        # 时间|等级(长度8左对齐)|输出log的文件名(长度15左对齐):行号|log信息
        formatter = logging.Formatter(
            "%(asctime)s|%(levelname)-8s|%(filename)-15s:%(lineno)4s|%(message)s"
        )

        # 将设置好的格式应用到处理器
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # 将处理器添加到logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger


logger = Logger().create_logger()
pass