# if __name__=="__main__":
#     import sys
#     app =QtWidgets.QApplication(sys.argv)
#     MainWindow=QtWidgets.QMainWindow()
#     ui=Ui_Dialog()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


Form, Window = uic.loadUiType("tracker.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()



app.exec()

# C:\Python392\Lib\site-packages\PyQt4\pyuic4.bat -х tracker.ui -о tracker.py
# pip install
# РАБОТАЕТ ПРООВЕРЕНО делает из файла интерфейса файл ПИТОНА
# pyuic5 tracker.ui -o tracker.py