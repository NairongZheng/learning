import sys
from loguru import logger
from s7_2_module1 import Module1

# 定义主日志，所有日志都会记录到这里面，同时输出到控制台（这边的format都可以去掉，是我为了看后面的name跟module上下文而添加的）
logger.remove()
logger.add("./logs/main.log", rotation="1 MB", retention="10 days", mode="w", format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name: <15}:{function:<10}:{line:<3} - {extra} {message}")
logger.add(sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name: <15}:{function:<10}:{line:<3} - {extra} {message}")


def main():
    logger.info("main函数")
    module1 = Module1()
    module1.func1()
    module1.func2()


if __name__ == '__main__':
    main()