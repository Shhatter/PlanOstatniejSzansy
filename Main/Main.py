import sys
import random
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

gFCompliments = [
    "Najfajniejszy Kruszek na świecie",
    "Najmądrzejszy Kruszek",
    "Najlepiej zdający egzaminy Kruszek"
]
class MainDialog(QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        loadUi('main.ui', self)
        self.questionNumber = 0
        self.slideNumber = 0

        self.setWindowTitle(gFCompliments[ random.randint(0,len(gFCompliments)-1)])


app = QApplication(sys.argv)
widget = MainDialog()
widget.show()

print("Exit")
sys.exit(app.exec())
