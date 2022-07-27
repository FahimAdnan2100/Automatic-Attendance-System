import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QComboBox, QApplication
from PyQt5.QtTextToSpeech import QTextToSpeech
from output2 import Ui_OutputDialog2
from attendanceinfo import Ui_AttendanceDialog
import cv2
import face_recognition
import numpy as np
import datetime
import os
import csv
import mysql.connector
import pandas as pd
import pickle

class Ui_StudentDialog(QDialog):



    def __init__(self):
        super(Ui_StudentDialog, self).__init__()
        loadUi("./student.ui", self)
        self.runButton_5.clicked.connect(self.runSlot7)
        self.engine = None


        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()

        selectquery = "select * from depts"
        cursor.execute(selectquery)
        records = cursor.fetchall()
        depts = []
        depts.append('Select Department')
        # depts.append("Select Department")
        for row in records:
            dept = row[1]
            depts.append(dept)
        self.comboBox5.addItems(depts)
        dept_id = self.comboBox5.currentText()
        self.comboBox5.currentIndexChanged.connect(self.selectionchange)







    def selectionchange(self, i):
        self.comboBox1.clear()
        dept_id = self.comboBox5.currentText()
        #print(dept_id)

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()
        selectquery1 = "select * from depts "
        cursor.execute(selectquery1)
        record = cursor.fetchall()
        for row in record:
            self.aa = row[1]
            if (self.aa == dept_id):
                self.bb = row[0]
                #print(self.bb)
                break

        batchs = []
        batchs.append('Select Batch No')
        for i in range(1, 31):
            batchs.append(str(i))
        #print(batchs)
        self.comboBox1.addItems(batchs)
        self.comboBox1.currentIndexChanged.connect(self.selectionchange1)


    def selectionchange1(self,b):
        self.comboBox2.clear()
        batch_no = self.comboBox1.currentText()
        #print('dept_id:',self.bb)
        #print('batch_no:', batch_no)
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()
        selectcourse = "select * from courses"
        cursor.execute(selectcourse)
        records = cursor.fetchall()
        self.courses = []
        #self.courses.append('Select Course')
        # depts.append("Select Department")
        for row in records:
            if self.bb == row[1] and batch_no == row[2]:
                course = row[3]
                self.courses.append(course)


        self.comboBox2.addItems(self.courses)

        self.course_no = self.comboBox2.currentText()
        print(self.course_no)
        self.runButton_3.clicked.connect(self.train)
        self.runButton_2.clicked.connect(self.runSlot5)
        self.runButton_4.clicked.connect(self.runSlot6)

        #runButton_4

        self._new_window = None
        self.Videocapture_ = None

    def info(self):
        #print(self.content)
        self.d = self.comboBox5.currentText()
        self.b = self.comboBox1.currentText()
        self.c = self.comboBox2.currentText()
        print(self.d)
        print(self.b)
        print(self.c)

    def refreshAll(self):
        self.Videocapture_ = "0"
        #self.Videocapture_ = "rtsp://admin:HZQRBI@192.168.0.106"
        #self.Videocapture_ = "http://admin:HZQRBI@192.168.0.105"

    @pyqtSlot()

    def train(self):

        # speech
        self.engine = None
        engineNames = QTextToSpeech.availableEngines()
        if len(engineNames) > 0:
            engineNames = engineNames[0]
            self.engine = QTextToSpeech(engineNames)
        self.voices = []
        for voice in self.engine.availableVoices():
            self.voices.append(voice)
        self.engine.setVoice(self.voices[0])

        self.d = self.comboBox5.currentText()
        self.b = self.comboBox1.currentText()
        self.c = self.comboBox2.currentText()


        print(self.d)
        print(self.d)

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()
        selectquery1 = "select * from depts "
        cursor.execute(selectquery1)
        record = cursor.fetchall()
        # self.a=[]
        print(self.d)
        for row in record:
            if self.d == row[1]:
                self.a = row[0]
                print(self.a)
                break

        selectquery = "select * from student_infos"
        cursor.execute(selectquery)
        records = cursor.fetchall()
        # known face encoding and known face name list
        images = []
        self.class_names = []
        self.student_id = []
        self.encode_list = []

        # self.k = 0
        for row in records:
            self.all_depts = row[3]
            self.all_batch = row[4]

            if self.all_depts == self.a and self.all_batch == self.b:
                b = 'D:/xampp8.28/htdocs/AttendanceSystem/Laravel/AttendenceSystem/public/'
                s = row[7]

                print(b)
                s = (b + s)
                # s = s[7:]
                print(s)
                curImg = cv2.imread(s, 1)
                images.append(curImg)
                self.class_names.append(row[1])
                self.student_id.append(row[2])
                print(self.class_names)
        #
        self.engine.say('Image Training Started')
        item=[]
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]

            #print(encodes_cur_frame)

            # encode = face_recognition.face_encodings(img)[0]
            self.encode_list.append(encodes_cur_frame)
            #self.k = self.k + 1
            #print(self.k)
            a=encodes_cur_frame
            item.append(a)
        with open(self.d+self.b+'faces', 'wb') as fp:
            pickle.dump(item, fp)

        self.engine.say('Image Training Finished')


    def runSlot5(self):
        print("Clicked Run")

        self.info()
        self.refreshAll()
        print(self.Videocapture_)

        self.outputWindow2_()  # Create and open new output window
        self.close()
        #self.out()
    def runSlot6(self):
        print("Clicked Run")

        self.info()
        self.refreshAll()


        self.outputWindow3_()  # Create and open new output window
        self.close()
        #self.out()


    def outputWindow2_(self):
        self._new_window = Ui_OutputDialog2()
        self._new_window.show()
        self._new_window.info(self.d,self.b,self.c)
        self._new_window.startVideo(self.Videocapture_)
        print("Video Played")


    def outputWindow3_(self):
        self._new_window = Ui_AttendanceDialog()
        self._new_window.show()
        self._new_window.info(self.d,self.b,self.c)
        print("Attendance Info")
    def runSlot7(self):
        print("Clicked Run main")


        self.outputWindow9_()  # Create and open new output window
        self.close()
        # self.out()

    def outputWindow9_(self):
        from mainwindow import Ui_Dialog
        self._new_window = Ui_Dialog()

        self._new_window.show()


        print("Video Played")



