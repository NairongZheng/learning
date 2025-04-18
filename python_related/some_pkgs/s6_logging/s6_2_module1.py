import logging
# from s6_1_logger_with_code import logger
from s6_1_logger_with_ini import logger
import s6_3_module2
import s6_4_module3


def main():
    # 只要前面有from s6_1_logger_with_ini import logger，就设置过log的格式了，这里直接用logging也行
    logger.info("这是module1的打印")
    s6_3_module2.main()
    s6_4_module3.main()
    pass


if __name__ == '__main__':
    main()