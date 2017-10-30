import sys
from PyQt5 import QtWidgets
from gui.LoginWindow import Ui_LoginForm


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


class QtChatView:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self.login_window = LoginDialog()

    def get_username(self):
        self.login_window.show()
        self._app.exec_()
        return self.login_window.username
