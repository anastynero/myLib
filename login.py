from PyQt5.Qt import *

from welcome import MainWindow
from signup import Dialog
import sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Авторизация")
        Dialog.resize(496, 265)
        Dialog.setStyleSheet("background-color: rgb(255, 196, 246)")
        self.u_name_label = QLabel(Dialog)
        self.u_name_label.setGeometry(QRect(150, 110, 71, 20))
        self.u_name_label.setStyleSheet("font: 12pt \"Segoe Script\";")
        self.pass_label = QLabel(Dialog)
        self.pass_label.setGeometry(QRect(140, 150, 75, 21))
        self.pass_label.setStyleSheet("font: 12pt \"Segoe Script\";")
        self.uname_lineEdit = QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QRect(230, 110, 113, 20))
        self.pass_lineEdit = QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QRect(230, 150, 113, 20))
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.login_btn = QPushButton(Dialog)
        self.login_btn.setGeometry(QRect(170, 200, 60, 30))
        self.login_btn.setStyleSheet("background-color: white")
        self.signup_btn = QPushButton(Dialog)
        self.signup_btn.setStyleSheet("background-color: white")
        self.signup_btn.setGeometry(QRect(250, 200, 120, 30))
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(140, 10, 211, 51))
        self.label.setStyleSheet("font: 16pt \"Segoe Script\";")


        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.u_name_label.setText(_translate("Dialog", "Логин"))
        self.pass_label.setText(_translate("Dialog", "Пароль"))
        self.login_btn.setText(_translate("Dialog", "Войти"))
        self.signup_btn.setText(_translate("Dialog", "Регистрация"))
        self.label.setText(_translate("Dialog", "Авторизация"))


class LoginDatabase():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def is_table(self, table_name):
        query = "SELECT name from sqlite_master WHERE type='table' AND name='{}';".format(table_name)
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.loginDatabase = LoginDatabase('login.db')
        if self.loginDatabase.is_table('USERS'):
            pass
        else:
            self.loginDatabase.conn.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, EMAIL TEXT, PASSWORD TEXT)")
            self.loginDatabase.conn.execute("INSERT INTO USERS VALUES(?, ?, ?)",
                                           ('admin', 'admin@gmail.com', 'admin')
            )
            self.loginDatabase.conn.commit()

        self.login_btn.clicked.connect(self.loginCheck)
        self.signup_btn.clicked.connect(self.signUpCheck)

    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def welcomeWindowShow(self, username):
        self.welcomeWindow = MainWindow(username)
        self.welcomeWindow.show()

    def signUpShow(self):
        self.signUpWindow = Dialog(self)
        self.signUpWindow.show()

    def loginCheck(self):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()
        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return

        result = self.loginDatabase.conn.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",
                                                 (username, password))
        if len(result.fetchall()):
            self.welcomeWindowShow(username)
            self.hide()
            self.loginDatabase.conn.close()
        else:
            self.showMessageBox('Внимание!', 'Неправильное имя пользователя или пароль.')

    def signUpCheck(self):
        self.signUpShow()


if __name__ == "__main__":
    import sys
    app    = QApplication(sys.argv)
    w = MainDialog()
    w.show()
    sys.exit(app.exec_())