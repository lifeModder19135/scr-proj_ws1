from client import createclient, get_aggs
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import sys

# run code from client.py
get_aggs(createclient())

# run code from gui.py
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
