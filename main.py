from client import createclient
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import sys

# run code from client.py
createclient()

# run code from gui.py
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    #script.py

    print('hello world')

    #tasks.py

    from invoke import task

@task
def build(c):
   print('Building!')

@task
def hello(c):
   c.run('./script.py')