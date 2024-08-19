# pyqt

[参考链接](https://www.bilibili.com/video/BV1WV4y1J79w)

1. p4：qt入门
2. password_generator：密码生成小程序
3. json_formatter：json小工具


## 设计流程
1. 先用QT设计师设计好界面：QT设计师：E:\app_installation\anaconda\install\envs\pytorch\Lib\site-packages\PySide2\designer.exe
2. 把ui文件转成python文件：`pyuic6 password_generator.ui -o password_generator.py`
3. 编写界面与逻辑分离的程序
4. 打包成exe：`pyinstaller -F -w p9_password_generator_main.py`