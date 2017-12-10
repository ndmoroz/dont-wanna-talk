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
        self.current_tab = self._create_new_tab('FirstChatTab')
        self._ui.ChatsTabWidget.removeTab(0)
        self._ui.SendButton.clicked.connect(self.get_new_message)
        self._ui.SendButton.setShortcut('Ctrl+Return')
        self._ui.SendButton.setToolTip('Ctrl+Enter')
        # self._ui.ChatsTabWidget.tabBarClicked.connect(self.read_new_message)
        self._ui.action_add_friend.triggered.connect(self.add_contact)
        self._ui.ContactsListWidget.itemClicked.connect(self.activate_chat)
        # self._ui.SendButton.clicked.connect(self._create_new_tab)

    def start(self):
        friend_list = self.client.get_friend_list()
        for friend in friend_list:
            self._ui.ContactsListWidget.addItem(friend)
        self.show()

    def get_new_message(self):
        message = self._ui.MessagePlainTextEdit.toPlainText()
        self.print_message(self.client.user_name, message)
        self.client.write_message(message)
        self._ui.MessagePlainTextEdit.clear()

    def read_new_message(self):
        self.print_message(
            self.client.rfile.readline().strip().decode('utf-8'))

    def print_message(self, user, message):
        current_chat_text = self.current_tab.ui.ChatPlainTextEdit
        current_chat_text.moveCursor(QtGui.QTextCursor.End)

        bold_font = QtGui.QTextCharFormat()
        bold_font.setFontWeight(QtGui.QFont.Bold)
        current_chat_text.setCurrentCharFormat(bold_font)
        current_chat_text.insertPlainText(user + '>')

        normal_font = QtGui.QTextCharFormat()
        normal_font.setFontWeight(QtGui.QFont.Normal)
        current_chat_text.setCurrentCharFormat(normal_font)
        current_chat_text.insertPlainText(message + '\n')
        current_chat_text.moveCursor(QtGui.QTextCursor.End)

    def add_contact(self):
        items = self.client.get_all_contacts()
        item, ok = QtWidgets.QInputDialog. \
            getItem(None,  # parent
                    "Adding new friend",  # title
                    "Friend to add",  # label
                    items,  # items
                    0,  # default
                    False)  # editable
        if ok and item:
            self._ui.ContactsListWidget.addItem(item)
            self.client.add_friend(item)

    def _create_new_tab(self, tab_title):
        new_tab = ChatTab()
        self._ui.ChatsTabWidget.addTab(new_tab, tab_title)
        return new_tab

    def activate_chat(self, selected_chat):
        chat_name = selected_chat.text()
        self._create_new_tab(chat_name)


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
        self.chat_window.start()
        # self.chat_window.show()
        self._app.exec_()

    def set_client(self, client_model):
        self.chat_window.client = client_model
