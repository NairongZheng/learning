"""
    密码生成小程序的主代码文件
"""
import sys
import string
import random
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from p8_password_generator import Ui_PasswordGenerator


class MyPasswordGenerator(Ui_PasswordGenerator, QDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.show()

        self.pushButton.clicked.connect(self.new_password)

    def new_password(self):
        words = (string.digits
                 + string.ascii_uppercase
                 + string.ascii_lowercase
                 + string.punctuation)

        words = random.sample(list(words), 20)
        password = "".join(words)
        self.lineEdit.setText(password)
        QMessageBox.information(self, "信息提示", "密码生成成功")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myPasswordGenerator = MyPasswordGenerator()

    sys.exit(app.exec())
