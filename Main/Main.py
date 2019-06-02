import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class MainDialog(QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('raz dwa trzy')


app = QApplication(sys.argv)
widget = MainDialog()
widget.show()

print("Exit")
sys.exit(app.exec())
