# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatTab.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.ChatPlainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.ChatPlainTextEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ChatPlainTextEdit.sizePolicy().hasHeightForWidth())
        self.ChatPlainTextEdit.setSizePolicy(sizePolicy)
        self.ChatPlainTextEdit.setMinimumSize(QtCore.QSize(150, 20))
        self.ChatPlainTextEdit.setReadOnly(True)
        self.ChatPlainTextEdit.setObjectName("ChatPlainTextEdit")
        self.gridLayout.addWidget(self.ChatPlainTextEdit, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

