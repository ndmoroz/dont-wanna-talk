import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from gui.LoginWindow import Ui_LoginForm
from gui.ChatWindow import Ui_ChatMainWindow
from gui.ChatTab import Ui_Form


class LoginDialog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.username = ''
        self.password = ''
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.ui.LoginLineEdit.returnPressed.connect(self.enter_pressed)
        self.ui.PasswordLineEdit.returnPressed.connect(self.enter_pressed)

    def enter_pressed(self):
        self.username = self.ui.LoginLineEdit.text()
        self.password = self.ui.PasswordLineEdit.text()
        self.close()


class ChatTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class ChatWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self._ui = Ui_ChatMainWindow()
        self._ui.setupUi(self)
        self._create_new_tab()
        self._ui.ChatsTabWidget.removeTab(0)
        self._ui.SendButton.clicked.connect(self.get_new_message)
        self._ui.ChatsTabWidget.tabBarClicked.connect(self.read_new_message)
        self._ui.action_add_friend.triggered.connect(self.add_contact)
        # self._ui.SendButton.clicked.connect(self._create_new_tab)

    def get_new_message(self):
        self.client.write_message(
            self._ui.MessagePlainTextEdit.toPlainText())
        self._ui.MessagePlainTextEdit.clear()

    def read_new_message(self):
        self.print_message(
            self.client.rfile.readline().strip().decode('utf-8'))

    def print_message(self, message):
        self._ui.ChatPlainTextEdit.moveCursor(QtGui.QTextCursor.End)
        self._ui.ChatPlainTextEdit.insertPlainText(message + '\n')
        self._ui.ChatPlainTextEdit.moveCursor(QtGui.QTextCursor.End)

    def add_contact(self):
        # items = ("friend1", "friend2", "friend3")
        items = self.client.get_all_contacts()
        item, ok = QtWidgets.QInputDialog.getItem(
            self, "select input dialog", "list of languages", items, 0, False)
        if ok and item:
            self._ui.ContactsListWidget.addItem(item)

    def _create_new_tab(self):
        newTab = ChatTab()
        self._ui.ChatsTabWidget.addTab(newTab, 'NewTab')


class QtChatView:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self.login_window = LoginDialog()
        self.chat_window = ChatWindow()

    def get_username(self):
        self.login_window.show()
        self._app.exec_()
        return self.login_window.username

    def show_chat(self):
        self.chat_window.show()
        self._app.exec_()

    def set_client(self, client_model):
        self.chat_window.client = client_model
