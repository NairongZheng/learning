
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QHBoxLayout, QMessageBox


def show_msg():
    QMessageBox.information(window, "信息提示", "你点击了我")


if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建一个QT应用程序，sys.argv表示可以从命令行传参数进来
    window = QDialog()              # 这样才有界面
    window.resize(400, 300)         # (h, w)

    hbox = QHBoxLayout()
    button = QPushButton('点击我')      # 添加按钮
    button.clicked.connect(show_msg)    # 添加函数响应

    hbox.addWidget(button)          # 把button放进去
    window.setLayout(hbox)

    window.show()                   # 展示界面窗口
    sys.exit(app.exec())            # 可以启动app，然后再退出
