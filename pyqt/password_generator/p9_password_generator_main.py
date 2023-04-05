"""
    密码生成小程序的主代码文件
    添加功能：
    1. 给密码设置不同网站
    2. 可以选择大写字母、小写字母、数字、标点
    3. 生成后导出到txt文件
"""
import sys
import string
import random
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from p9_password_generator import Ui_PasswordGenerator


class MyPasswordGenerator(Ui_PasswordGenerator, QDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.show()

        self.pushButton.clicked.connect(self.new_password)

    def new_password(self):
        site = self.lineEdit_site.text()
        if not site:
            QMessageBox.warning(self, "信息提示", "请输入site")
            return
        
        words = []
        if self.checkBox_upper.isChecked():             # * 2是怕不够20位
            words.append(string.ascii_uppercase * 2)
        if self.checkBox_lower.isChecked():
            words.append(string.ascii_lowercase * 2)
        if self.checkBox_number.isChecked():
            words.append(string.digits * 2)
        if self.checkBox_puc.isChecked():
            words.append(string.punctuation * 2)

        if not words:       # 没有选的话就默认要所有元素
            words = (string.digits
                    + string.ascii_uppercase
                    + string.ascii_lowercase
                    + string.punctuation)
        else:
            words = "".join(words)

        words = random.sample(list(words), 20)
        password = "".join(words)
        self.lineEdit_result.setText(password)

        with open("我的密码本.txt", "a", encoding="utf8") as f:
            f.write(f"{site}\t{password}\n")

        QMessageBox.information(self, "信息提示", "密码生成成功")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myPasswordGenerator = MyPasswordGenerator()

    sys.exit(app.exec())
