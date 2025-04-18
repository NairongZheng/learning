# logging日志

只要代码运行起来，有设置过logger，后续在不同子脚本中引用logger或者直接用logging都可以，会继承格式的
其实正常开发直接用loguru就可以了，省的自己定义

1. s6_1_logger_with_code.py：直接在代码定义logger
2. s6_1_logger_with_ini.py：用ini配置文件定义logger