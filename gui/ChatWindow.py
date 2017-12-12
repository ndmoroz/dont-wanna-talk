# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatMainWindow(object):
    def setupUi(self, ChatMainWindow):
        ChatMainWindow.setObjectName("ChatMainWindow")
        ChatMainWindow.resize(278, 154)
        ChatMainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(ChatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ContactsListWidget = QtWidgets.QListWidget(
            self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ContactsListWidget.sizePolicy().hasHeightForWidth())
        self.ContactsListWidget.setSizePolicy(sizePolicy)
        self.ContactsListWidget.setMinimumSize(QtCore.QSize(75, 0))
        self.ContactsListWidget.setBaseSize(QtCore.QSize(0, 0))
        self.ContactsListWidget.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.ContactsListWidget.setObjectName("ContactsListWidget")
        self.verticalLayout_3.addWidget(self.ContactsListWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setBaseSize(QtCore.QSize(0, 1000))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setOpaqueResize(True)
        self.splitter_2.setChildrenCollapsible(True)
        self.splitter_2.setObjectName("splitter_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.splitter_2)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ChatsTabWidget = QtWidgets.QTabWidget(
            self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ChatsTabWidget.sizePolicy().hasHeightForWidth())
        self.ChatsTabWidget.setSizePolicy(sizePolicy)
        self.ChatsTabWidget.setObjectName("ChatsTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ChatPlainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.ChatPlainTextEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ChatPlainTextEdit.sizePolicy().hasHeightForWidth())
        self.ChatPlainTextEdit.setSizePolicy(sizePolicy)
        self.ChatPlainTextEdit.setMinimumSize(QtCore.QSize(150, 20))
        self.ChatPlainTextEdit.setObjectName("ChatPlainTextEdit")
        self.horizontalLayout.addWidget(self.ChatPlainTextEdit)
        self.ChatsTabWidget.addTab(self.tab, "")
        self.horizontalLayout_3.addWidget(self.ChatsTabWidget)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.splitter_2)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.MessagePlainTextEdit = QtWidgets.QPlainTextEdit(
            self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MessagePlainTextEdit.sizePolicy().hasHeightForWidth())
        self.MessagePlainTextEdit.setSizePolicy(sizePolicy)
        self.MessagePlainTextEdit.setMinimumSize(QtCore.QSize(75, 25))
        self.MessagePlainTextEdit.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.MessagePlainTextEdit.setObjectName("MessagePlainTextEdit")
        self.horizontalLayout_4.addWidget(self.MessagePlainTextEdit)
        self.SendButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout_4.addWidget(self.SendButton)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        ChatMainWindow.setCentralWidget(self.centralwidget)
        self.action_add_friend = QtWidgets.QAction(ChatMainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/add_user_icon"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_friend.setIcon(icon)
        self.action_add_friend.setObjectName("action_add_friend")
        self.ContactsListWidget.addAction(self.action_add_friend)

        self.retranslateUi(ChatMainWindow)
        self.ChatsTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ChatMainWindow)

    def retranslateUi(self, ChatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatMainWindow.setWindowTitle(
            _translate("ChatMainWindow", "DontWannaTalk Chat"))
        self.ChatsTabWidget.setTabText(self.ChatsTabWidget.indexOf(self.tab),
                                       _translate("ChatMainWindow", "Tab 1"))
        self.SendButton.setText(_translate("ChatMainWindow", "Send"))
        self.action_add_friend.setText(
            _translate("ChatMainWindow", "Add friend"))
        self.action_add_friend.setToolTip(_translate("ChatMainWindow",
                                                     "Adds new friend to your contact list"))
