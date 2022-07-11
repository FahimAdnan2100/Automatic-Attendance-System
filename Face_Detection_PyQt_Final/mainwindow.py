import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
import resource
from out_window import Ui_OutputDialog
from out_window1 import Ui_OutputDialog1
from student import Ui_StudentDialog
from PyQt5.QtTextToSpeech import QTextToSpeech
import mysql.connector

class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("mainwindow.ui", self)

        self.engine = None
        engineNames = QTextToSpeech.availableEngines()
        if len(engineNames) > 0:
            engineNames = engineNames[0]
            self.engine = QTextToSpeech(engineNames)
        self.voices = []
        for voice in self.engine.availableVoices():
            self.voices.append(voice)
        self.engine.setVoice(self.voices[0])
        #self.engine.say('Automatic Attendance system using Face Recognition Started')
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()
        selectquery = "select * from depts"
        cursor.execute(selectquery)
        records = cursor.fetchall()
        depts = []
        #depts.append("Select Department")
        for row in records:
            dept = row[1]
            depts.append(dept)
        # print(depts)
        self.comboBox.addItems(depts)
        self.runButton.clicked.connect(self.runSlot)
        self.runButton_2.clicked.connect(self.runSlot2)
        self.runButton_3.clicked.connect(self.runSlot3)
        self._new_window = None
        self.Videocapture_ = None

    def dept(self):
        #print(self.content)
        self.content = self.comboBox.currentText()

    def refreshAll(self):
        self.Videocapture_ = "0"
        #self.Videocapture_ = "rtsp://admin:HZQRBI@192.168.0.106"
        #self.Videocapture_ = "http://admin:HZQRBI@192.168.0.105"

    @pyqtSlot()
    def runSlot(self):
        print("Clicked Run")
        self.dept()
        self.refreshAll()
        print(self.Videocapture_)
        ui.hide()  # hide the main window
        self.outputWindow_()  # Create and open new output window
        #self.out()
    def runSlot2(self):
        print("Clicked 2 Run")

        self.refreshAll()
        print(self.Videocapture_)
        ui.hide()  # hide the main window
        self.outputWindow_1()  # Create and open new output window
        #self.out()
    def runSlot3(self):
        print("Clicked Student Run")


        ui.hide()  # hide the main window
        self.student()  # Create and open new output window
        #self.out()


    def outputWindow_(self):
        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        self._new_window.dept(self.content)
        self._new_window.startVideo(self.Videocapture_)
        print("Video Played")
    def outputWindow_1(self):
        self._new_window = Ui_OutputDialog1()
        self._new_window.show()

        self._new_window.startVideo(self.Videocapture_)
        print("Video Played")
    def student(self):
        self._new_window = Ui_StudentDialog()

        self._new_window.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()

    sys.exit(app.exec_())

