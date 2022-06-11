from PyQt5.Qt import *


class Ui_signUp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Регистрация")
        Dialog.resize(570, 375)
        Dialog.setStyleSheet("background-color: rgb(255, 196, 246)")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(160, 130, 81, 31))
        self.label.setStyleSheet("font: 12pt \"Segoe Script\";")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(160, 230, 81, 31))
        self.label_2.setStyleSheet("font: 12pt \"Segoe Script\";")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(160, 180, 81, 31))
        self.label_3.setStyleSheet("font: 12pt \"Segoe Script\";")
        self.label_3.setObjectName("label_3")
        self.uname_lineEdit = QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QRect(250, 130, 141, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.email_lineEdit = QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QRect(250, 180, 141, 20))
        self.password_lineEdit = QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QRect(250, 230, 141, 20))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.signup_btn = QPushButton(Dialog)
        self.signup_btn.setGeometry(QRect(230, 290, 140, 30))
        self.signup_btn.setStyleSheet("background-color: white")
        self.label_4 = QLabel(Dialog)
        self.label_4.setStyleSheet("font: 16pt \"Segoe Script\";")
        self.label_4.setGeometry(QRect(130, 10, 321, 81))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Регистрация"))
        self.label.setText(_translate("Dialog", "Логин"))
        self.label_2.setText(_translate("Dialog", "Пароль"))
        self.label_3.setText(_translate("Dialog", "Email"))
        self.signup_btn.setText(_translate("Dialog", "Зарегистрироваться"))
        self.label_4.setText(_translate("Dialog", "Создать профиль"))


class Dialog(QDialog, Ui_signUp):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.signup_btn.clicked.connect(self.insertData)

    @pyqtSlot()
    def insertData(self):
        username = self.uname_lineEdit.text()
        email    = self.email_lineEdit.text()
        password = self.password_lineEdit.text()

        if (not username) or (not email) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля')
            return

        result = self.parent.loginDatabase.conn.execute("SELECT * FROM USERS WHERE USERNAME = ?", (username,))
        if result.fetchall():
            msg = QMessageBox.information(self, 'Внимание!', 'Пользователь с таким именем уже зарегистрирован')
        else:
            self.parent.loginDatabase.conn.execute("INSERT INTO USERS VALUES(?, ?, ?)",
                                                   (username, email, password))
            self.parent.loginDatabase.conn.commit()
            self.close()


if __name__ == "__main__":
    import sys
    app    = QApplication(sys.argv)
    w = Dialog()
    w.show()

    sys.exit(app.exec_())