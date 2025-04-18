"""
在配置文件定义logger
"""
import logging
import logging.config
import os

class Logger:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logging.ini")
        self.reset()

    def reset(self):
        # 创建日志目录
        cur_dir_path = os.path.dirname(os.path.abspath(__file__))
        self.log_path = os.path.join(cur_dir_path, "logs")
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

    def create_logger(self):
        logging.config.fileConfig(self.config_path)
        return logging.getLogger()

# 使用配置后的logger
logger = Logger().create_logger()
pass