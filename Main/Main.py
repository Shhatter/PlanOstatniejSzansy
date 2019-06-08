import sys
import random
import datetime
import calendar
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtWidgets import QApplication, QDialog, QCalendarWidget, QVBoxLayout
from PyQt5.uic import loadUi

gFCompliments = [
    "Najfajniejszy Kruszek na świecie",
    "Najmądrzejszy Kruszek",
    "Najlepiej zdający egzaminy Kruszek"
]


class MainDialog(QDialog):

    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        self.dFrom = None
        self.dTo = None
        self.questionNumber = 0
        self.slideNumber = 0
        self.setWindowTitle(gFCompliments[random.randint(0, len(gFCompliments) - 1)])
        # self.dateFrom = None
        # self.dateTo = None
        self.initUi()

    def initUi(self):

        self.dateFrom.selectionChanged.connect(self.changeDateFrom)
        self.dateTo.selectionChanged.connect(self.changeDateTo)
        self.dateFrom.setGridVisible(True)
        self.dateTo.setGridVisible(True)
        self.dateTo.setSelectedDate(QtCore.QDate.currentDate().addDays(1))

        self.dFrom = self.dateFrom.selectedDate().toPyDate()
        self.dTo= self.dateTo.selectedDate().toPyDate()
        # print(tempD1,tempD2)
        # self.dFrom = QDate(tempD1).toPyDate()
        # self.dTo=   QDate(tempD2).toPyDate()
        print(self.dFrom, self.dTo)

        self.dateFromLabel.setText(self.dateFrom.selectedDate().toString())
        self.dateToLabel.setText(self.dateTo.selectedDate().toString())

        self.logOutput.appendPlainText("Start")
        self.logOutput.setReadOnly(True)

        end_date = QtCore.QDate.currentDate()
        # self.resetButton.connect(self.__init__())

    def changeDateFrom(self):
        self.dateFromLabel.setText(self.dateFrom.selectedDate().toString())
        self.dFrom = self.dateFrom.selectedDate().toPyDate()
        print("dFrom",self.dFrom)

        return None

    def changeDateTo(self):
        self.dateToLabel.setText(self.dateTo.selectedDate().toString())
        self.dTo= self.dateTo.selectedDate().toPyDate()
        print("dTo",self.dTo)
        return None

    def recalculateData(self):


        return None


app = QApplication(sys.argv)
widget = MainDialog()
widget.show()

print("Exit")
sys.exit(app.exec())
