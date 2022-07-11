from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtTextToSpeech import QTextToSpeech
import cv2
import face_recognition
import numpy as np
import datetime
import os
import csv
import mysql.connector
import pandas as pd

class Ui_OutputDialog1(QDialog):
    def __init__(self):
        super(Ui_OutputDialog1, self).__init__()
        loadUi("./automatic.ui", self)

        self.image = None
        date_time_string1 = datetime.datetime.now().strftime("%y_%m_%d")
        date_time_string_d = datetime.datetime.now().strftime("%d")
        date_time_string_m = datetime.datetime.now().strftime("%b")
        date_time_string_y = datetime.datetime.now().strftime("%Y")

        path = 'Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '.csv'
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w+') as f:
                pass

    @pyqtSlot()
    def startVideo(self, camera_name):
        print(cv2.useOptimized())
        if len(camera_name) == 1:
            self.capture = cv2.VideoCapture(int(camera_name))
        else:
            self.capture = cv2.VideoCapture(camera_name)
        self.timer = QTimer(self)  # Create Timer
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

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()
        selectquery1 = "select * from depts "
        cursor.execute(selectquery1)
        record = cursor.fetchall()
        self.a=[]
        for row in record:
            self.a.append(row[0])
        print(self.a)
        selectquery = "select * from teacher_infos"
        cursor.execute(selectquery)
        records = cursor.fetchall()
        # known face encoding and known face name list
        images = []
        self.class_names = []
        self.encode_list = []

        self.k = 0
        for row in records:
            self.all_depts = row[2]
            for self.r in self.a:
                if self.all_depts == self.r:
                    b = 'E:/New folder/Face-Recogntion-PyQt-master/Face-Recogntion-PyQt-master/AttendanceSystem/Laravel/AttendenceSystem/public/'
                    s = row[3]
                    print(b)
                    s = (b + s)
                    # s = s[7:]
                    print(s)
                    curImg = cv2.imread(s, 1)
                    images.append(curImg)
                    self.class_names.append(row[1])
                    print(self.class_names)

        self.engine.say('Image Training Started')
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            print(encodes_cur_frame)

            # encode = face_recognition.face_encodings(img)[0]
            self.encode_list.append(encodes_cur_frame)
            self.k = self.k + 1
            # print(self.k)
        self.engine.say('Image Training Finished')
        self.timer.timeout.connect(self.update_frame)  # Connect timeout to the output function
        self.timer.start(10)  # emit the timeout() signal at x=40ms

    def face_rec_(self, frame, encode_list_known, class_names):
        date_time_string1 = datetime.datetime.now().strftime("%y_%m_%d")
        date_time_string_d = datetime.datetime.now().strftime("%d")
        date_time_string_m = datetime.datetime.now().strftime("%b")
        date_time_string_y = datetime.datetime.now().strftime("%Y")


        def mark_attendance(name):
                path = 'Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '.csv'
                with open(path,'r+') as f:
                    myDataList = f.readlines()
                    nameList = []
                    date_time_string = datetime.datetime.now().strftime("%H:%M")
                    timeList=[]

                    for line in myDataList:
                        entry = line.split(',')
                        nameList.append(entry[0])
                        #timeList.append(entry[0])
                    if name not in nameList:

                        f.writelines(f'\n{name},{date_time_string}')


        imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_cur_frame = face_recognition.face_locations(imgS)
        encodes_cur_frame = face_recognition.face_encodings(imgS, faces_cur_frame)
        # print(faces_cur_frame)
        # count = 0
        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=.6)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
            # print(face_dis)
            best_match_index = np.argmin(face_dis)
            # print("s",best_match_index)
            if match[best_match_index]:
                name = class_names[best_match_index].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                #cv2.putText(frame, str(match), (x1 + 6, y2 + 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0), 1)
                mark_attendance(name)
            else:
                name = 'Unknown'
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        return frame

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.displayImage(self.image, self.encode_list, self.class_names, 1)

    def displayImage(self, image, encode_list, class_names, window=1):
        image = cv2.resize(image, (640, 480))
        try:
            image = self.face_rec_(image, encode_list, class_names)
        except Exception as e:
            print(e)
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.imgLabel1.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel1.setScaledContents(True)