# Form implementation generated from reading ui file 'json_formatter.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_JsonFormatter(object):
    def setupUi(self, JsonFormatter):
        JsonFormatter.setObjectName("JsonFormatter")
        JsonFormatter.resize(727, 533)
        JsonFormatter.setStyleSheet("* {\n"
"font-size:16px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(JsonFormatter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=JsonFormatter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit_json = QtWidgets.QPlainTextEdit(parent=JsonFormatter)
        self.plainTextEdit_json.setObjectName("plainTextEdit_json")
        self.verticalLayout.addWidget(self.plainTextEdit_json)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_format = QtWidgets.QPushButton(parent=JsonFormatter)
        self.pushButton_format.setObjectName("pushButton_format")
        self.horizontalLayout.addWidget(self.pushButton_format)
        self.pushButton_unformat = QtWidgets.QPushButton(parent=JsonFormatter)
        self.pushButton_unformat.setObjectName("pushButton_unformat")
        self.horizontalLayout.addWidget(self.pushButton_unformat)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_copyjson = QtWidgets.QPushButton(parent=JsonFormatter)
        self.pushButton_copyjson.setObjectName("pushButton_copyjson")
        self.verticalLayout.addWidget(self.pushButton_copyjson)

        self.retranslateUi(JsonFormatter)
        QtCore.QMetaObject.connectSlotsByName(JsonFormatter)

    def retranslateUi(self, JsonFormatter):
        _translate = QtCore.QCoreApplication.translate
        JsonFormatter.setWindowTitle(_translate("JsonFormatter", "JSON格式化小工具"))
        self.label.setText(_translate("JsonFormatter", "请输入粘贴JSON文本："))
        self.pushButton_format.setText(_translate("JsonFormatter", "格式化JSON"))
        self.pushButton_unformat.setText(_translate("JsonFormatter", "反格式化JSON"))
        self.pushButton_copyjson.setText(_translate("JsonFormatter", "复制JSON内容"))
