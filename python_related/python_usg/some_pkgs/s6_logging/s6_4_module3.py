# from s6_1_logger_with_code import logger
import logging

def main():
    # 通过s6_2_module1.py调用这个代码，会自动继承logger的设置，再import一次logger也行
    logger = logging.getLogger(__name__)
    logger.info("这是module3的打印")
    # 甚至直接用logging.info都可以
