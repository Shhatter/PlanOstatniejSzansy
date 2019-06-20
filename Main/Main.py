import sys
import random
import datetime
import math
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QCalendarWidget, QVBoxLayout, QDialogButtonBox
from PyQt5.uic import loadUi

gFCompliments = [
    "Najfajniejszy Kruszek na świecie",
    "Najmądrzejszy Kruszek",
    "Najlepiej zdający egzaminy Kruszek",
    "Nikt tak nie grzeje jak Kruszek"

]


class MainDialog(QDialog):

    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        self.dFrom = datetime.date.today()
        self.dTo = datetime.date.today() + datetime.timedelta(days=1)
        self.questionNumber = 0
        self.slideNumber = 0

        self.pon = False
        self.wto = False
        self.sro = False
        self.czw = False
        self.pio = False
        self.sob = False
        self.nie = False

        self.setWindowTitle(gFCompliments[random.randint(0, len(gFCompliments) - 1)])
        # self.dateFrom = None
        # self.dateTo = None
        self.initUi()

    def initUi(self):
        self.sNum.setText(str(self.slideNumber))
        self.pNum.setText(str(self.questionNumber))
        self.dateFrom.selectionChanged.connect(self.changeDateFrom)
        self.dateTo.selectionChanged.connect(self.changeDateTo)
        self.dateFrom.setGridVisible(True)
        self.dateTo.setGridVisible(True)
        self.dateTo.setSelectedDate(QtCore.QDate.currentDate().addDays(1))

        self.dFrom = self.dateFrom.selectedDate().toPyDate()
        self.dTo = self.dateTo.selectedDate().toPyDate()
        # print(tempD1,tempD2)
        # self.dFrom = QDate(tempD1).toPyDate()
        # self.dTo=   QDate(tempD2).toPyDate()
        print(self.dFrom, self.dTo)

        self.dateFromLabel.setText(self.dateFrom.selectedDate().toString())
        self.dateToLabel.setText(self.dateTo.selectedDate().toString())

        self.logOutput.appendPlainText("Start")
        self.logOutput.appendPlainText("Pamiętaj by data początku była przed datą końca :) ")

        self.logOutput.setReadOnly(True)

        end_date = QtCore.QDate.currentDate()
        # self.resetButton.connect(self.__init__())

        self.ponBox.stateChanged.connect(self.dayCheck)
        self.wtoBox.stateChanged.connect(self.dayCheck)
        self.sroBox.stateChanged.connect(self.dayCheck)
        self.czwBox.stateChanged.connect(self.dayCheck)
        self.pioBox.stateChanged.connect(self.dayCheck)
        self.sobBox.stateChanged.connect(self.dayCheck)
        self.nieBox.stateChanged.connect(self.dayCheck)

        self.subSlideNbr.clicked.connect(self.subSlide)
        self.addSlideNbr.clicked.connect(self.addSlide)
        self.subQuestionNbr.clicked.connect(self.subQuestion)
        self.addQuestionNbr.clicked.connect(self.addQuestion)

        self.menuOptions.button(QDialogButtonBox.Reset).clicked.connect(self.resetApp)
        self.menuOptions.button(QDialogButtonBox.Ok).clicked.connect(self.calulateData)

    def resetApp(self):
        print("Reset All Data")
        self.dFrom = datetime.date.today()
        self.dTo = datetime.date.today() + datetime.timedelta(days=1)
        self.questionNumber = 0
        self.slideNumber = 0

        self.dateFrom.setSelectedDate(QtCore.QDate.currentDate())
        self.dateTo.setSelectedDate(QtCore.QDate.currentDate().addDays(1))

        self.pNum.setText(str("0"))
        self.sNum.setText(str("0"))
        self.pon = False
        self.wto = False
        self.sro = False
        self.czw = False
        self.pio = False
        self.sob = False
        self.nie = False

        self.ponBox.setChecked(False)
        self.wtoBox.setChecked(False)
        self.sroBox.setChecked(False)
        self.czwBox.setChecked(False)
        self.pioBox.setChecked(False)
        self.sobBox.setChecked(False)
        self.nieBox.setChecked(False)

        self.changeSlide.clear()
        self.changeQuestion.clear()

        self.logOutput.appendPlainText("Reset Danych")

    def subSlide(self):

        temp = str(self.changeSlide.toPlainText()).replace(" ", "")
        if (str(temp).isdigit()):
            if ((self.slideNumber - int(temp)) < 0):
                self.slideNumber = 0
                self.sNum.setText(str(self.slideNumber))
            else:
                self.slideNumber -= int(temp)
                self.sNum.setText(str(self.slideNumber))
        else:
            self.logOutput.appendPlainText("nieprawidłowa wartość w polu - musi być to tylko liczba całkowita")

        self.changeSlide.clear()
        print("temp", temp)

    def addSlide(self):

        temp = str(self.changeSlide.toPlainText()).replace(" ", "")
        if (str(temp).isdigit()):
            self.slideNumber += int(temp)
            self.sNum.setText(str(self.slideNumber))
        else:
            self.logOutput.appendPlainText("nieprawidłowa wartość w polu - musi być to tylko liczba całkowita")

        self.changeSlide.clear()
        print("temp", temp)

    def subQuestion(self):

        temp = str(self.changeQuestion.toPlainText()).replace(" ", "")
        if (str(temp).isdigit()):
            if ((self.questionNumber - int(temp)) < 0):
                self.questionNumber = 0
                self.pNum.setText(str(self.questionNumber))
            else:
                self.questionNumber -= int(temp)
                self.pNum.setText(str(self.questionNumber))
        else:
            self.logOutput.appendPlainText("nieprawidłowa wartość w polu - musi być to tylko liczba całkowita")
        self.changeQuestion.clear()
        print("temp", temp)

    def addQuestion(self):

        temp = str(self.changeQuestion.toPlainText()).replace(" ", "")
        if (str(temp).isdigit()):
            self.questionNumber += int(temp)
            self.pNum.setText(str(self.questionNumber))
        else:
            self.logOutput.appendPlainText("nieprawidłowa wartość w polu - musi być to tylko liczba całkowita")

        self.changeQuestion.clear()
        print("temp", temp)

    def changeDateFrom(self):
        self.dateFromLabel.setText(self.dateFrom.selectedDate().toString())
        self.dFrom = self.dateFrom.selectedDate().toPyDate()
        print("dFrom", self.dFrom)

        return None

    def changeDateTo(self):
        self.dateToLabel.setText(self.dateTo.selectedDate().toString())
        self.dTo = self.dateTo.selectedDate().toPyDate()

        print("dTo", self.dTo)
        return None

    def calulateData(self):
        self.logOutput.appendPlainText("--------------------------------------------------------")

        undoFlag = False;
        # obliczenie ile dni jest faktycznej nauki
        if (self.questionNumber == 0 and self.slideNumber == 0):
            self.logOutput.appendPlainText("Nie dodano żadnych pytań !")
            undoFlag = True

        if (self.dFrom >= self.dTo):
            self.logOutput.appendPlainText("Data początku nie może być większa bądź równa dacie końca !")
            print("dateFrom before dateTo", self.dFrom)
            undoFlag = True

        if (
                self.pon == False and self.wto == False and self.sro == False and self.czw == False and self.pio == False and self.sob == False and self.nie == False):
            self.logOutput.appendPlainText("Nie wybrano żadnego dnia w tygodniu na naukę !")
            undoFlag = True

        if undoFlag:
            return None

        daysCounter = 0
        dFromTemp = self.dFrom

        while dFromTemp != self.dTo:
            if (dFromTemp.weekday() == 0 and self.pon == True):
                daysCounter += 1

            if (dFromTemp.weekday() == 1 and self.wto == True):
                daysCounter += 1
            if (dFromTemp.weekday() == 2 and self.sro == True):
                daysCounter += 1
            if (dFromTemp.weekday() == 3 and self.czw == True):
                daysCounter += 1
            if (dFromTemp.weekday() == 4 and self.pio == True):
                daysCounter += 1
            if (dFromTemp.weekday() == 5 and self.sob == True):
                daysCounter += 1
            if (dFromTemp.weekday() == 6 and self.nie == True):
                daysCounter += 1
            dFromTemp = dFromTemp + datetime.timedelta(days=1)

        self.logOutput.appendPlainText("ilość dni nauki: " + str(daysCounter))

        if (self.slideNumber != 0):
            slidesPerDay = self.slideNumber / daysCounter
            if int(slidesPerDay) == slidesPerDay:
                self.logOutput.appendPlainText("Ilość slajdów do przerobienia dziennie: " + str(slidesPerDay))
            else:

                missingslides = self.slideNumber - (math.floor(slidesPerDay) * daysCounter)
                self.logOutput.appendPlainText(
                    "Ilość slajdów do przerobienia dziennie: " + str(math.floor(slidesPerDay)))
                if missingslides == 1:
                    self.logOutput.appendPlainText("z czego pierwszego dnia trzeba zrobić dodatkowo 1 dodatkowy slajd")
                else:
                    self.logOutput.appendPlainText(
                        "z czego, pierwszego dnia trzeba zrobić dodatkowo " + str(missingslides) + " slajdy")

        if (self.questionNumber != 0):
            questionsPerDay = self.questionNumber / daysCounter
            if int(questionsPerDay) == questionsPerDay:
                self.logOutput.appendPlainText("Ilość pytań do przerobienia dziennie: " + str(questionsPerDay))
            else:
                missingQuestions = self.questionNumber - (math.floor(questionsPerDay) * daysCounter)
                self.logOutput.appendPlainText(
                    "Ilość pytań do przerobienia dziennie: " + str(math.floor(questionsPerDay)))
                if missingQuestions == 1:
                    self.logOutput.appendPlainText(
                        "z czego, pierwszego dnia trzeba zrobić dodatkowo 1 dodatkowe pytanie")
                else:
                    self.logOutput.appendPlainText(
                        "z czego pierwszego dnia trzeba zrobić dodatkowo " + str(missingQuestions) + " pytania")
        # if (self.dFrom >= self.dTo):
        #     self.logOutput.appendPlainText("Data końca nie może być przed datą początku !")
        #     print("dateFrom before dateTo", self.dFrom)
        #     return None
        self.logOutput.appendPlainText("--------------------------------------------------------")

        return None

    def dayCheck(self):
        try:
            if (self.pon != self.ponBox.isChecked()):
                self.pon = self.ponBox.isChecked()
                print("pon Changed", self.pon)

            if (self.wto != self.wtoBox.isChecked()):
                self.wto = self.wtoBox.isChecked()
                print("wto Changed", self.wto)

            if (self.sro != self.sroBox.isChecked()):
                self.sro = self.sroBox.isChecked()
                print("sro Changed", self.sro)

            if (self.czw != self.czwBox.isChecked()):
                self.czw = self.czwBox.isChecked()
                print("czw Changed", self.czw)

            if (self.pio != self.pioBox.isChecked()):
                self.pio = self.pioBox.isChecked()
                print("pio Changed", self.pio)

            if (self.sob != self.sobBox.isChecked()):
                self.sob = self.sobBox.isChecked()
                print("sob Changed", self.sob)

            if (self.nie != self.nieBox.isChecked()):
                self.nie = self.nieBox.isChecked()
                print("nie changed", self.nie)
        except:
            print("An exception occurred")


app = QApplication(sys.argv)
widget = MainDialog()
widget.show()

print("Exit")
sys.exit(app.exec())
