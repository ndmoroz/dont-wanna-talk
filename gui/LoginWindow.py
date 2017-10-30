# -*- coding: utf-8 -*-

# Form implementation generated from reading _ui file 'LoginWindow._ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(300, 38)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            LoginForm.sizePolicy().hasHeightForWidth())
        LoginForm.setSizePolicy(sizePolicy)
        LoginForm.setMinimumSize(QtCore.QSize(0, 38))
        LoginForm.setMaximumSize(QtCore.QSize(16777215, 38))
        self.horizontalLayout = QtWidgets.QHBoxLayout(LoginForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoginLineEdit = QtWidgets.QLineEdit(LoginForm)
        self.LoginLineEdit.setText("")
        self.LoginLineEdit.setReadOnly(False)
        self.LoginLineEdit.setObjectName("LoginLineEdit")
        self.horizontalLayout.addWidget(self.LoginLineEdit)
        self.PasswordLineEdit = QtWidgets.QLineEdit(LoginForm)
        self.PasswordLineEdit.setText("")
        self.PasswordLineEdit.setReadOnly(False)
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.horizontalLayout.addWidget(self.PasswordLineEdit)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(
            _translate("LoginForm", "Hit «enter» when ready"))
        self.LoginLineEdit.setPlaceholderText(_translate("LoginForm", "Name"))
        self.PasswordLineEdit.setPlaceholderText(
            _translate("LoginForm", "Password"))
