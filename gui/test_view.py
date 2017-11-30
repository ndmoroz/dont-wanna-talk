import sys
from PyQt5 import QtWidgets, QtGui
from gui.ChatWindow import Ui_ChatMainWindow
from gui.ChatTab import Ui_Form


class ChatTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class ChatWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_ChatMainWindow()
        self.ui.setupUi(self)
        self.create_new_tab()
        self.ui.ChatsTabWidget.removeTab(0)
        # self._ui.SendButton.clicked.connect(self.click_send)
        self.ui.action_add_friend.triggered(self.add_contact)
        self.ui.SendButton.clicked.connect(self.create_new_tab)

    def click_send(self):
        self.ui.ChatPlainTextEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.ChatPlainTextEdit.insertPlainText(
            self.ui.MessagePlainTextEdit.toPlainText() + '\n')
        self.ui.ChatPlainTextEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.MessagePlainTextEdit.clear()

    def add_contact(self):
        self.ui.ContactsListWidget.addItem(
            self.ui.MessagePlainTextEdit.toPlainText())

    def create_new_tab(self):
        newTab = ChatTab()
        self.ui.ChatsTabWidget.addTab(newTab, 'NewTab')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    slider = ChatWindow()
    slider.show()
    sys.exit(app.exec_())
