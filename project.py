from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from login import *
from signup import *
from welcome import *
import sqlite3


class Widget_1(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Widget_1, self).__init__(parent)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('Найти')
        self.btn.setStyleSheet("background-color: rgb(255, 196, 246);""font: 14pt ;")
        self.btn.setGeometry(QtCore.QRect(920, 20, 120, 40))
        self.btn.clicked.connect(self.res)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 900, 40))
        self.lineEdit.setStyleSheet("font: 14pt ;")
        self.lineEdit.setObjectName("поисковая строка")
        self.lineEdit.setStyleSheet("background-color: white")
        self.lineEdit.setPlaceholderText('Введите название книги')
        self.strList = ['Мастер и Маргарита', 'Вино из одуванчиков', 'Гарри Поттер и философский камень',
                        'Война и мир', 'Горе от ума', '1984', 'Три товарища', 'Бойцовский клуб', 'Над пропастью во ржи',
                        'Унесенные ветром', 'Крестный отец', 'Граф Монте-Кристо', 'Зелёная миля', 'Властелин колец',
                        'Буря мечей']
        completer = QCompleter(self.strList, self.lineEdit)
        self.lineEdit.setCompleter(completer)

        # виджеты #
        conn = sqlite3.connect('books.db')
        curs = conn.cursor()
        window1 = curs.execute('SELECT * FROM books WHERE id=1').fetchone()
        window2 = curs.execute('SELECT * FROM books WHERE id=2').fetchone()
        window3 = curs.execute('SELECT * FROM books WHERE id=3').fetchone()
        window4 = curs.execute('SELECT * FROM books WHERE id=4').fetchone()
        # окно 1 #
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 90, 461, 271))
        self.widget.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.title1 = QtWidgets.QLabel(self.widget)
        self.title1.setGeometry(QtCore.QRect(20, 5, 415, 41))
        self.title1.setStyleSheet("font: 12pt \"Segoe Print\";")
        self.title1.setText(window1[1])
        self.des1 = QtWidgets.QTextBrowser(self.widget)
        self.des1.setGeometry(QtCore.QRect(200, 60, 251, 201))
        self.des1.setStyleSheet("font: 8pt \"Segoe Print\";" "background-color: rgb(255, 255, 255);")
        self.des1.setText(window1[3])
        self.img1 = QtWidgets.QLabel(self.widget)
        self.img1.setGeometry(QtCore.QRect(20, 60, 160, 180))
        self.pic1 = QPixmap(str(window1[4])).scaled(160, 180)
        self.img1.setPixmap(self.pic1)
        self.author1 = QtWidgets.QLabel(self.widget)
        self.author1.setGeometry(QtCore.QRect(20, 240, 180, 25))
        self.author1.setStyleSheet(" font: 10pt \"Segoe Print\";")
        self.author1.setText(window1[2])
        # окно 2 #
        self.widget_3 = QtWidgets.QWidget(self)
        self.widget_3.setGeometry(QtCore.QRect(580, 90, 461, 271))
        self.widget_3.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.title2 = QtWidgets.QLabel(self.widget_3)
        self.title2.setGeometry(QtCore.QRect(110, 10, 361, 41))
        self.title2.setText(window2[1])
        self.title2.setStyleSheet(" font: 12pt \"Segoe Print\";")
        self.des2 = QtWidgets.QTextBrowser(self.widget_3)
        self.des2.setGeometry(QtCore.QRect(200, 60, 251, 201))
        self.des2.setStyleSheet("background-color: rgb(255, 255, 255); font: 8pt \"Segoe Print\";")
        self.des2.setText(window2[3])
        self.img2 = QtWidgets.QLabel(self.widget_3)
        self.img2.setGeometry(QtCore.QRect(10, 60, 160, 180))
        self.pic2 = QPixmap(str(window2[4])).scaled(160, 180)
        self.img2.setPixmap(self.pic2)
        self.author2 = QtWidgets.QLabel(self.widget_3)
        self.author2.setGeometry(QtCore.QRect(20, 240, 180, 25))
        self.author2.setText(window2[2])
        self.author2.setStyleSheet(" font: 10pt \"Segoe Print\";")
        # окно 3 #
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setGeometry(QtCore.QRect(20, 400, 461, 271))
        self.widget_2.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.title3 = QtWidgets.QLabel(self.widget_2)
        self.title3.setGeometry(QtCore.QRect(170, 10, 361, 41))
        self.title3.setText(str(window3[1]))
        self.title3.setStyleSheet(" font: 12pt \"Segoe Print\";")
        self.des3 = QtWidgets.QTextBrowser(self.widget_2)
        self.des3.setText(window3[3])
        self.des3.setGeometry(QtCore.QRect(200, 60, 251, 201))
        self.des3.setStyleSheet("background-color: rgb(255, 255, 255); font: 8pt \"Segoe Print\";")
        self.img3 = QtWidgets.QLabel(self.widget_2)
        self.img3.setGeometry(QtCore.QRect(10, 60, 160, 180))
        self.pic3 = QPixmap(str(window3[4])).scaled(160, 180)
        self.img3.setPixmap(self.pic3)
        self.author3 = QtWidgets.QLabel(self.widget_2)
        self.author3.setGeometry(QtCore.QRect(20, 240, 180, 25))
        self.author3.setText(window3[2])
        self.author3.setStyleSheet(" font: 10pt \"Segoe Print\";")
        # окно 4 #
        self.widget_5 = QtWidgets.QWidget(self)
        self.widget_5.setGeometry(QtCore.QRect(580, 400, 461, 271))
        self.widget_5.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.title4 = QtWidgets.QLabel(self.widget_5)
        self.title4.setText(window4[1])
        self.title4.setGeometry(QtCore.QRect(160, 10, 361, 41))
        self.title4.setStyleSheet(" font: 12pt \"Segoe Print\";")
        self.des4 = QtWidgets.QTextBrowser(self.widget_5)
        self.des4.setText(window4[3])
        self.des4.setGeometry(QtCore.QRect(200, 60, 251, 201))
        self.des4.setStyleSheet("background-color: rgb(255, 255, 255); font: 8pt \"Segoe Print\";")
        self.img4 = QtWidgets.QLabel(self.widget_5)
        self.img4.setGeometry(QtCore.QRect(10, 60, 160, 180))
        self.pic4 = QPixmap(str(window4[4])).scaled(160, 180)
        self.img4.setPixmap(self.pic4)
        self.author4 = QtWidgets.QLabel(self.widget_5)
        self.author4.setGeometry(QtCore.QRect(20, 240, 180, 25))
        self.author4.setText(window4[2])
        self.author4.setStyleSheet(" font: 10pt \"Segoe Print\";")
        # главный виджет #
        self.widgetMain = QtWidgets.QWidget(self)
        self.widgetMain.setGeometry(QtCore.QRect(80, 90, 931, 551))
        self.widgetMain.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.titleMain = QtWidgets.QLabel(self.widgetMain)
        self.titleMain.setGeometry(QtCore.QRect(10, 10, 601, 51))
        self.titleMain.setStyleSheet("font: 16pt \"Segoe Print\";")
        self.desMain = QtWidgets.QTextBrowser(self.widgetMain)
        self.desMain.setGeometry(QtCore.QRect(410, 70, 511, 471))
        self.desMain.setStyleSheet("background-color: rgb(255, 255, 255); font: 12pt \"Segoe Print\";")
        self.imgMain = QtWidgets.QLabel(self.widgetMain)
        self.imgMain.setGeometry(QtCore.QRect(40, 150, 301, 361))
        self.authorMain = QtWidgets.QLabel(self.widgetMain)
        self.authorMain.setGeometry(QtCore.QRect(10, 70, 391, 51))
        self.authorMain.setStyleSheet("font: 14pt \"Segoe Print\";")
        self.widgetMain.setVisible(False)

    # вывод основного виджета #
    def res(self):
        con = sqlite3.connect('books.db')
        cur = con.cursor()
        result = cur.execute('SELECT * FROM books WHERE title=?', (self.lineEdit.text(),)).fetchone()
        self.widget.setVisible(False)
        self.widget_2.setVisible(False)
        self.widget_3.setVisible(False)
        self.widget_5.setVisible(False)
        self.widgetMain.setVisible(True)
        self.picMain = QPixmap(str(result[4])).scaled(301, 361)
        self.imgMain.setPixmap(self.picMain)
        self.titleMain.setText(result[1])
        self.authorMain.setText(result[2])
        self.desMain.setText(result[3])


class Widget_2(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Widget_2, self).__init__()
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(650, 640, 161, 41))
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Добавить книгу')
        self.pushButton.clicked.connect(self.want_list)
        self.del_button = QtWidgets.QPushButton(self)
        self.del_button.setGeometry(QtCore.QRect(850, 640, 161, 41))
        self.del_button.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.del_button.setObjectName("delete")
        self.del_button.setText('Удалить книгу')
        self.del_button.clicked.connect(self.delete_item)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setStyleSheet("background-color: white")
        self.lineEdit.setGeometry(QtCore.QRect(200, 640, 451, 41))
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(5, 1, 1045, 600))
        self.listWidget.setObjectName("textBrowser")
        self.listWidget.setStyleSheet((("background-color: white;\n"
                                          "font: 16pt \"Segoe Print\";")))
    # добавление книги в список #
    def want_list(self):
        self.item = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.addItem(self.item)
    # удаление книги #
    def delete_item(self):
        clicked = self.listWidget.currentRow()
        self.listWidget.takeItem(clicked)

class Widget_3(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Widget_3, self).__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1031, 131))
        self.groupBox.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.groupBox.setObjectName("groupBox")
        self.text1 = QtWidgets.QTextEdit(self.groupBox)
        self.text1.setGeometry(QtCore.QRect(330, 10, 361, 111))
        self.text1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text1.setObjectName("textEdit")
        self.text1.setPlaceholderText("Впечатления о книге")
        self.line1 = QtWidgets.QLineEdit(self.groupBox)
        self.line1.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.line1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line1.setObjectName("lineEdit")
        self.line1.setPlaceholderText("Название книги")
        self.b1 = QtWidgets.QPushButton(self.groupBox)
        self.b1.setGeometry(QtCore.QRect(80, 70, 141, 31))
        self.b1.setStyleSheet("background-color: rgb(222, 154, 245);")
        self.b1.setObjectName("pushButton")
        self.b1.setText('Сохранить')
        self.b1.clicked.connect(self.saveMessage)
        self.quotes1 = QtWidgets.QTextEdit(self.groupBox)
        self.quotes1.setPlaceholderText("Цитаты")
        self.quotes1.setGeometry(QtCore.QRect(720, 10, 281, 111))
        self.quotes1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quotes1.setObjectName("textEdit_4")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox2 = QtWidgets.QGroupBox(self)
        self.groupBox2.setGeometry(QtCore.QRect(10, 150, 1031, 131))
        self.groupBox2.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.groupBox2.setObjectName("groupBox_2")
        self.text2 = QtWidgets.QTextEdit(self.groupBox2)
        self.text2.setGeometry(QtCore.QRect(330, 10, 361, 111))
        self.text2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text2.setObjectName("textEdit_2")
        self.text2.setPlaceholderText("Впечатления о книге")
        self.line2 = QtWidgets.QLineEdit(self.groupBox2)
        self.line2.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.line2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line2.setObjectName("lineEdit_2")
        self.line2.setPlaceholderText("Название книги")
        self.b2 = QtWidgets.QPushButton(self.groupBox2)
        self.b2.setGeometry(QtCore.QRect(80, 70, 141, 31))
        self.b2.setStyleSheet("background-color: rgb(222, 154, 245);")
        self.b2.setObjectName("pushButton_2")
        self.b2.setText('Сохранить')
        self.b2.clicked.connect(self.saveMessage)
        self.quotes2 = QtWidgets.QTextEdit(self.groupBox2)
        self.quotes2.setGeometry(QtCore.QRect(720, 10, 281, 111))
        self.quotes2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quotes2.setObjectName("textEdit_5")
        self.quotes2.setPlaceholderText("Цитаты")
        self.verticalLayout.addWidget(self.groupBox2)
        self.groupBox3 = QtWidgets.QGroupBox(self)
        self.groupBox3.setGeometry(QtCore.QRect(10, 290, 1031, 131))
        self.groupBox3.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.groupBox3.setObjectName("groupBox_3")
        self.text3 = QtWidgets.QTextEdit(self.groupBox3)
        self.text3.setGeometry(QtCore.QRect(330, 10, 361, 111))
        self.text3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text3.setObjectName("textEdit_3")
        self.text3.setPlaceholderText("Впечатления о книге")
        self.line3 = QtWidgets.QLineEdit(self.groupBox3)
        self.line3.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.line3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line3.setObjectName("lineEdit_3")
        self.line3.setPlaceholderText("Название книги")
        self.b3 = QtWidgets.QPushButton(self.groupBox3)
        self.b3.setGeometry(QtCore.QRect(80, 70, 141, 31))
        self.b3.setStyleSheet("background-color: rgb(222, 154, 245);")
        self.b3.setObjectName("pushButton_3")
        self.b3.setText('Сохранить')
        self.b3.clicked.connect(self.saveMessage)
        self.quotes3 = QtWidgets.QTextEdit(self.groupBox3)
        self.quotes3.setGeometry(QtCore.QRect(720, 10, 281, 111))
        self.quotes3 .setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quotes3 .setObjectName("textEdit_6")
        self.quotes3 .setPlaceholderText("Цитаты")
        self.verticalLayout.addWidget(self.groupBox3)
        self.groupBox4 = QtWidgets.QGroupBox(self)
        self.groupBox4.setGeometry(QtCore.QRect(10, 430, 1031, 131))
        self.groupBox4.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.groupBox4.setObjectName("groupBox_4")
        self.text4 = QtWidgets.QTextEdit(self.groupBox4)
        self.text4.setGeometry(QtCore.QRect(330, 10, 361, 111))
        self.text4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text4.setObjectName("textEdit_7")
        self.text4.setPlaceholderText("Впечатления о книге")
        self.line4 = QtWidgets.QLineEdit(self.groupBox4)
        self.line4.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.line4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line4.setObjectName("lineEdit_4")
        self.line4.setPlaceholderText("Название книги")
        self.b4 = QtWidgets.QPushButton(self.groupBox4)
        self.b4.setGeometry(QtCore.QRect(80, 70, 141, 31))
        self.b4.setStyleSheet("background-color: rgb(222, 154, 245);")
        self.b4.setObjectName("pushButton_4")
        self.b4.setText('Сохранить')
        self.b4.clicked.connect(self.saveMessage)
        self.quotes4 = QtWidgets.QTextEdit(self.groupBox4)
        self.quotes4.setGeometry(QtCore.QRect(720, 10, 281, 111))
        self.quotes4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quotes4.setObjectName("textEdit_8")
        self.quotes4.setPlaceholderText("Цитаты")
        self.verticalLayout.addWidget(self.groupBox4)
        self.groupBox5 = QtWidgets.QGroupBox(self)
        self.groupBox5.setGeometry(QtCore.QRect(10, 570, 1031, 131))
        self.groupBox5.setStyleSheet("background-color: rgb(255, 196, 246);")
        self.groupBox5.setObjectName("groupBox_5")
        self.text5 = QtWidgets.QTextEdit(self.groupBox5)
        self.text5.setGeometry(QtCore.QRect(330, 10, 361, 111))
        self.text5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text5.setObjectName("textEdit_9")
        self.text5.setPlaceholderText("Впечатления о книге")
        self.line5 = QtWidgets.QLineEdit(self.groupBox5)
        self.line5.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.line5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line5.setObjectName("lineEdit_5")
        self.line5.setPlaceholderText("Название книги")
        self.b5 = QtWidgets.QPushButton(self.groupBox5)
        self.b5.setGeometry(QtCore.QRect(80, 70, 141, 31))
        self.b5.setStyleSheet("background-color: rgb(222, 154, 245);")
        self.b5.setObjectName("pushButton_5")
        self.b5.setText('Сохранить')
        self.b5.clicked.connect(self.saveMessage)
        self.quotes5 = QtWidgets.QTextEdit(self.groupBox5)
        self.quotes5.setGeometry(QtCore.QRect(720, 10, 281, 111))
        self.quotes5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quotes5.setObjectName("textEdit_10")
        self.quotes5.setPlaceholderText("Цитаты")
        self.verticalLayout.addWidget(self.groupBox5)

    def saveMessage(self):
        save = QMessageBox()
        save.setWindowTitle('Сохранение')
        save.setText('Запись сохранена')
        save.setStyleSheet("background-color: rgb(255, 196, 246);")
        save.setStandardButtons(QMessageBox.Ok)
        save.exec_()




class Widget_4(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(Widget_4, self).__init__(parent)

        self.widgetProfile = QtWidgets.QWidget(self)
        self.label = QtWidgets.QLabel(self.widgetProfile)
        self.label.setGeometry(QtCore.QRect(300, 50, 430, 41))
        self.label.setStyleSheet("font: 18pt \"Segoe Script\";")
        self.label.setText('У вас уже есть аккаунт?')
        self.pushButton = QtWidgets.QPushButton(self.widgetProfile)
        self.pushButton.setGeometry(QtCore.QRect(400, 140, 190, 80))
        self.pushButton.setText('Войти')
        self.pushButton.setStyleSheet("background-color: rgb(255, 196, 246);\n"
                                          "font: 12pt \"Segoe Script\";")
        self.pushButton.clicked.connect(self.openDialog)
        self.label_2 = QtWidgets.QLabel(self.widgetProfile)
        self.label_2.setGeometry(QtCore.QRect(260, 315, 600, 41))
        self.label_2.setStyleSheet("font: 18pt \"Segoe Script\";")
        self.label_2.setText('Первый раз скачали приложение?')
        self.pushButton_2 = QtWidgets.QPushButton(self.widgetProfile)
        self.pushButton_2.setText('Зарегистрироваться')
        self.pushButton_2.setGeometry(QtCore.QRect(370, 400, 250, 80))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 196, 246);\n"
                                            "font: 12pt \"Segoe Script\";")
        self.pushButton_2.clicked.connect(self.sign)
        self.widgetProfile2 = QtWidgets.QWidget(self)
        self.widgetProfile2.setVisible(False)
        self.pushButton3 = QtWidgets.QPushButton(self.widgetProfile2)
        self.pushButton3.setText('Выйти')
        self.pushButton3.setGeometry(QtCore.QRect(370, 400, 250, 80))
        self.pushButton3.clicked.connect(self.exit)

    def exit(self):
        QApplication.quit()

    def openDialog(self):
        self.widgetProfile.setVisible(False)
        self.widgetProfile2.setVisible(True)
        dialog = MainDialog(self)
        dialog.exec_()

    def sign(self):
        self.widgetProfile.setVisible(False)
        self.widgetProfile2.setVisible(True)
        s = Dialog(self)
        s.exec_()

class Button(QtWidgets.QPushButton):
        pass




class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        page1 = Widget_1(self)

        page2 = Widget_2(self)
        page3 = Widget_3(self)
        page4 = Widget_4(self)



        options = ["Каталог", "Хочу прочитать", "Моя полка", "Профиль"]

        stackedwidget = QtWidgets.QStackedWidget()

        hlay = QtWidgets.QHBoxLayout()
        group = QtWidgets.QButtonGroup(self)
        group.buttonClicked[int].connect(stackedwidget.setCurrentIndex)

        for i, (option, widget) in enumerate(
                zip(
                    options,
                    (page1, page2, page3, page4)
                )

        ):

            button = Button(text=option, checkable=True)
            ix = stackedwidget.addWidget(widget)
            group.addButton(button, ix)
            hlay.addWidget(button)
            if i == 0:
                button.setChecked(True)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(stackedwidget)
        vbox.addLayout(hlay)

QSS = """
Button {
    background-color: #ffffff;
    font-size: 20px;
}
Button:checked {
    background-color: #de9af5;
}
QLabel {
    font-size: 30px;
    color: #000000;
}
"""


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    app.setStyleSheet(QSS)
    w = MainWindow()
    w.setStyleSheet("background-color: #de9af5")
    w.setWindowTitle('mylib')
    w.setWindowIcon(QtGui.QIcon('book.png'))
    w.setFixedSize(1081, 784)
    w.show()
    sys.exit(app.exec_())