# Form implementation generated from reading ui file 'p9_password_generator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(578, 390)
        self.verticalLayout = QtWidgets.QVBoxLayout(PasswordGenerator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=PasswordGenerator)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_site = QtWidgets.QLineEdit(parent=PasswordGenerator)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.lineEdit_site.setFont(font)
        self.lineEdit_site.setObjectName("lineEdit_site")
        self.horizontalLayout.addWidget(self.lineEdit_site)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_upper = QtWidgets.QCheckBox(parent=PasswordGenerator)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.checkBox_upper.setFont(font)
        self.checkBox_upper.setObjectName("checkBox_upper")
        self.horizontalLayout_2.addWidget(self.checkBox_upper)
        self.checkBox_lower = QtWidgets.QCheckBox(parent=PasswordGenerator)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.checkBox_lower.setFont(font)
        self.checkBox_lower.setObjectName("checkBox_lower")
        self.horizontalLayout_2.addWidget(self.checkBox_lower)
        self.checkBox_number = QtWidgets.QCheckBox(parent=PasswordGenerator)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.checkBox_number.setFont(font)
        self.checkBox_number.setObjectName("checkBox_number")
        self.horizontalLayout_2.addWidget(self.checkBox_number)
        self.checkBox_puc = QtWidgets.QCheckBox(parent=PasswordGenerator)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.checkBox_puc.setFont(font)
        self.checkBox_puc.setObjectName("checkBox_puc")
        self.horizontalLayout_2.addWidget(self.checkBox_puc)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(parent=PasswordGenerator)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.lineEdit_result = QtWidgets.QLineEdit(parent=PasswordGenerator)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(24)
        self.lineEdit_result.setFont(font)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.verticalLayout.addWidget(self.lineEdit_result)

        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "密码生成小程序"))
        self.label.setText(_translate("PasswordGenerator", "请输入网站名称："))
        self.checkBox_upper.setText(_translate("PasswordGenerator", "大写字母"))
        self.checkBox_lower.setText(_translate("PasswordGenerator", "小写字母"))
        self.checkBox_number.setText(_translate("PasswordGenerator", "数字"))
        self.checkBox_puc.setText(_translate("PasswordGenerator", "标点符号"))
        self.pushButton.setText(_translate("PasswordGenerator", "生成新的密码"))
