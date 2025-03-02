from client import createclient
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow

# run code from client.py
createclient()

# run code from gui.py
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())