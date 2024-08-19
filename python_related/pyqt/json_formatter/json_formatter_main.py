"""
    json格式化小程序的主代码文件
"""
import sys
import json
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
import json_formatter


class MyJsonFormatter(json_formatter.Ui_JsonFormatter, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_format.clicked.connect(self.do_format_json("format"))

        self.pushButton_unformat.clicked.connect(self.do_format_json("unformat"))

        self.pushButton_copyjson.clicked.connect(self.do_copy_json)


    def do_copy_json(self):
        board = QApplication.clipboard()
        board.setText(self.plainTextEdit_json.toPlainText())
        QMessageBox.information(self, "信息提示", "复制成功")


    def do_format_json(self, type):
        def inner_format():
            json_cont = self.plainTextEdit_json.toPlainText()
            if not json_cont:
                QMessageBox.warning(self, "信息提示", "请输入内容")
                return

            try:
                if type == "format":
                    new_cont = json.dumps(json.loads(
                        json_cont), indent=4, ensure_ascii=False)
                else:
                    new_cont = json.dumps(json.loads(
                        json_cont), ensure_ascii=False)
                self.plainTextEdit_json.setPlainText(new_cont)
            except Exception as e:
                QMessageBox.information(self, "信息提示", f"json文本有问题，加载报错：{e}")
                return

            QMessageBox.information(self, "信息提示", "操作成功")

        return inner_format


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myJsonFormatter = MyJsonFormatter()

    sys.exit(app.exec())


"""
{
    "小明": {
        "学号": 123,
        "性别": "男",
        "爱好": "学python"
    },
    "小红": {
        "学号": 124,
        "性别": "女",
        "爱好": "学java"
    }
}
"""
