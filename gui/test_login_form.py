import sys
from PyQt5 import QtWidgets
from gui.LoginWindow import Ui_LoginForm
from PyQt5 import QtCore


class LoginDialog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.ui.LoginLineEdit.returnPressed.connect(self.enter_pressed)
        self.ui.PasswordLineEdit.returnPressed.connect(self.enter_pressed)

    def enter_pressed(self):
        print(self.ui.LoginLineEdit.text() +
              ' ' + self.ui.PasswordLineEdit.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    slider = LoginDialog()
    slider.show()
    sys.exit(app.exec_())
