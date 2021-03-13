

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 614)
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 311, 341))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 281, 31))
        font = QtGui.QFont()
        font.setFamily("TonightRUS")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(341, 72, 361, 351))
        self.calendarWidget.setObjectName("calendarWidget")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 440, 711, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(70, 490, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 492, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Parsek")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 560, 691, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Программа Чунина Владимира  НАПОМИНАЛКА СОБЫТИЙ"))
        self.label.setText(_translate("Dialog", "ЧТО СДЕЛАТЬ МНЕ"))
        self.label_2.setText(_translate("Dialog", "ПЛАНИРОВКА СОБЫТИЙ "))
        self.pushButton.setText(_translate("Dialog", "Выполнить..."))
        self.label_3.setText(_translate("Dialog", "ВРЕМЯ ОСТАВШЕЕСЯ ДО ОКОНЧАНИЯ РАБОТЫ"))

if __name__=="__main__":
    import sys
    app =QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

