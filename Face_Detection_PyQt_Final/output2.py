from logging import Manager

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt5.QtWidgets import QDialog,QMessageBox,QListWidget
from PyQt5.QtTextToSpeech import QTextToSpeech
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import face_recognition
import numpy as np
import datetime
import os
import csv
import mysql.connector
import pandas as pd
from csv import reader
import pickle
import sys
import openpyxl
from string import ascii_uppercase

from PyQt5.uic.properties import QtWidgets


class Ui_OutputDialog2(QDialog):
    def __init__(self):
        super(Ui_OutputDialog2, self).__init__()
        loadUi("./outputwindow2.ui", self)

        #self.pushButton.clicked.connect(self.absent)
        #self.pushButton_3.clicked.connect(self.attendance)
        self.allatten=[]
        self.allatten1 = []
        self.tatt = []
        self.tabs = []
        self.cours=[]
        self.ts=[]
        self.ddt=[]
        self.header=[]
        self.ada=[]
        self.abs=[]
        self.nam=[]
        self.idd=[]
        self.pre=[]

        self.nam1 = []
        self.idd1 = []
        self.pre1 = []
        self.image = None

        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.verticalHeader().setVisible(False)
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

        self.pushButton_2.clicked.connect(self.runSlot6)

    def runSlot6(self):
        print("Clicked Run")

        self.outputWindow3_()

        self.close()
        # self.out()

    def outputWindow3_(self):
        from student import Ui_StudentDialog
        self._new_window = Ui_StudentDialog()

        self._new_window.show()

        print("Video Played")

    @pyqtSlot()
    def info(self,dd,bb,cc):
        self.d= dd
        self.b = bb
        self.c = cc
        date_time_string1 = datetime.datetime.now().strftime("%y_%m_%d")
        date_time_string_d = datetime.datetime.now().strftime("%d")
        date_time_string_m = datetime.datetime.now().strftime("%b")
        date_time_string_y = datetime.datetime.now().strftime("%Y")
        date_time_string_yy = datetime.datetime.now().strftime("%y")

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()
        selectquery8 = "select * from student_attendances where dept=%s and batch=%s and course_no=%s and year=%s and month=%s and date=%s"
        tt2 = (self.d, self.b, self.c, date_time_string_y, date_time_string_m, date_time_string_d)
        cursor.execute(selectquery8, tt2)
        arecords1 = cursor.fetchall()
        for rr1 in arecords1:
            if rr1 != '':
                self.allatten1.append(rr1[2] + ',' + rr1[1] + ',' + rr1[9]+'\n')

        self.label_2.setText('DATE :          '+date_time_string_d+', '+date_time_string_m+' '+date_time_string_y)
        date_time_string11 = datetime.datetime.now().strftime("%I:%M %p")
        self.label_4.setText('TIME :          ' + date_time_string11)
        self.label_3.setText('COURSE :     ' + self.c.upper())

        # attendace show in gui
        # total student attendance



        path = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 +'/'+self.d+'/'+self.b+'/'+self.c +'.csv'
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w+') as f:
                pass
        path1 = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '/' + self.d + '/' + self.b + '/' + self.c+'_absent' + '.csv'
        print(path1)
        if not os.path.exists(path1):
            os.makedirs(os.path.dirname(path1), exist_ok=True)
            with open(path1, 'w+') as f:
                pass
        path2 = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '/' + self.d + '/' + self.b + '/' + self.c + '_attendance' + '.csv'
        print(path2)
        if not os.path.exists(path2):
            os.makedirs(os.path.dirname(path2), exist_ok=True)
            with open(path2, 'w+') as f:
                pass

            
    def startVideo(self, camera_name):

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
        #self.a=[]
        #print(self.d)
        for row in record:
            if self.d==row[1]:
                self.a=row[0]
                #print(self.a)
                break

        selectquery = "select * from student_infos where dept_id = %s and batch=%s"
        dept_ba=(self.a,self.b)
        cursor.execute(selectquery,dept_ba)

        records = cursor.fetchall()
        #print(records)
        #known face encoding and known face name list
        images = []
        self.class_names = []
        self.student_id = []
        self.encode_list = []
        self.totalstudent=1
        self.k = 0
        for row in records:
            self.all_depts = row[3]
            self.all_batch = row[4]

            if self.all_depts == self.a and self.all_batch==self.b:
                #self.totalstudent=self.totalstudent+1
                #print('Total student is : ' + self.totalstudent)
                b = 'E:/New folder/Face-Recogntion-PyQt-master/Face-Recogntion-PyQt-master/AttendanceSystem/Laravel/AttendenceSystem/public/'
                s = row[7]

                #print(b)
                s = (b + s)
                # s = s[7:]
                #print(s)
                curImg = cv2.imread(s, 1)
                images.append(curImg)
                self.class_names.append(row[1])
                self.student_id.append(row[2])
                #print(self.class_names)
                self.sl=len(self.class_names)

        # self.engine.say('Image Training Started')
        # item=[]
        # for img in images:
        #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #     boxes = face_recognition.face_locations(img)
        #     encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
        #
        #     #print(encodes_cur_frame)
        #
        #     # encode = face_recognition.face_encodings(img)[0]
        #     self.encode_list.append(encodes_cur_frame)
        #     #self.k = self.k + 1
        #     #print(self.k)
        #     a=encodes_cur_frame
        #     item.append(a)
        # with open('outfile', 'wb') as fp:
        #     pickle.dump(item, fp)
        #
        # self.engine.say('Image Training Finished')
        #print(self.d+self.b+'faces')
        with open(self.d+self.b+'faces', 'rb') as fp:
            self.encode_list = pickle.load(fp)
        #print(self.encode_list)
        self.timer.timeout.connect(self.update_frame)  # Connect timeout to the output function
        self.timer.start(10)  # emit the timeout() signal at x=40ms
        self.ll_n = []
        self.ll_d = []
        self.k = 1
        self.nn = 1

        self.row2 = 0
        self.jj1 = 1



    def face_rec_(self, frame, encode_list_known, class_names,student_id):
        date_time_string1 = datetime.datetime.now().strftime("%y_%m_%d")
        date_time_string_d = datetime.datetime.now().strftime("%d")
        date_time_string_m = datetime.datetime.now().strftime("%b")
        date_time_string_y = datetime.datetime.now().strftime("%Y")
        date_time_string11 = datetime.datetime.now().strftime("%I:%M %p")
        self.label_4.setText('TIME :          '+date_time_string11)
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()
        tab = "select * from student_attendances where dept=%s and batch=%s and course_no=%s and year=%s and month=%s and date=%s"
        tt = (self.d, self.b, self.c, date_time_string_y, date_time_string_m, date_time_string_d)
        cursor.execute(tab, tt)
        records1 = cursor.fetchall()

        if self.nn == 1:
            for row in records1:
                self.tableWidget.setRowCount(self.jj1)
                qq=1
                n = row[1]
                ii=row[2]
                t = row[9]
                ss =str(self.k)+'. '+ii+' '+ n +'  Login at ' + t


                self.tableWidget.setItem(self.row2, 0, QTableWidgetItem(str(self.k)))
                self.tableWidget.setItem(self.row2, 1, QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(self.row2, 2, QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(self.row2, 3, QTableWidgetItem(str(row[9])))
                self.row2 = self.row2 + 1
                self.jj1 = self.jj1 + 1


                #self.listWidget.setForeground(Qt.red)
                self.k = self.k + 1
                qq+=1
            self.nn += 1

        def attendance(self):
            date_time_string1 = datetime.datetime.now().strftime("%y_%m_%d")
            date_time_string_d = datetime.datetime.now().strftime("%d")
            date_time_string_m = datetime.datetime.now().strftime("%b")
            date_time_string_y = datetime.datetime.now().strftime("%Y")
            date_time_string11 = datetime.datetime.now().strftime("%I:%M %p")
            path2 = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '/' + self.d + '/' + self.b + '/' + self.c + '_attendance' + '.csv'
            if (os.path.exists(path2) and os.path.isfile(path2)):
                os.remove(path2)
                print("file deleted")
            else:
                print("file not found")
            path2 = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '/' + self.d + '/' + self.b + '/' + self.c + '_attendance' + '.csv'
            if not os.path.exists(path2):
                os.makedirs(os.path.dirname(path2), exist_ok=True)
                with open(path2, 'w+') as f:
                    pass

            k = open(path2, 'r+')



            #si = self.allatten.count();
            k.writelines(self.cours)
            k.writelines(self.ddt)
            k.writelines(self.ts)
            k.writelines(self.tatt)
            k.writelines(self.tabs)
            k.writelines(self.header)
            k.writelines(self.allatten1)

            # attendace show in gui
            # total student attendance
            ats = str(self.ts[0])
            print(ats)
            xatx = ats.split(', ')
            self.label_5.setText( str(xatx[0]))
            self.label_6.setText( str(self.tatt[0]))
            self.label_7.setText(str(self.tabs[0]))

            for i in range(len(self.allatten)):
                n=self.allatten[i]
                #print(n)
                k.writelines(n)




            #k.writelines(f'\n{self.idd},{self.nam},{self.pre}\n')
            #k.writelines(self.ada)
            #k.writelines(self.abs)
            # i=0
            # for i in range(len(self.allatten)):
            #     print(self.allatten)
            #     for j in range(3):
            #
            #         k.writelines(f'\n{self.allatten[j]}')
            #                  #f',{self.allatten[i+1]},{self.allatten[i+2]}\n')
            #     i=i+3
            self.allatten.clear()
            self.idd.clear()
            self.nam.clear()
            self.pre.clear()
            self.idd1.clear()
            self.nam1.clear()
            self.pre1.clear()
            self.ddt.clear()



            #self.abs.clear()
            self.tatt.clear()
            self.tabs.clear()
            self.header.clear()
            self.ts.clear()
            self.cours.clear()
        def absent(self):

            date_time_string1 = datetime.datetime.now().strftime("%y_%m_%d")
            date_time_string_d = datetime.datetime.now().strftime("%d")
            date_time_string_m = datetime.datetime.now().strftime("%b")
            date_time_string_y = datetime.datetime.now().strftime("%Y")
            date_time_string11 = datetime.datetime.now().strftime("%I:%M %p")

            path = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '/' + self.d + '/' + self.b + '/' + self.c + '_absent' + '.csv'
            f = open(path, 'a+')

            f.truncate(0)

            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
            cursor = self.conn.cursor()

            selectquery10 = "select * from student_attendances where dept=%s and batch=%s and course_no=%s and year=%s and month=%s and date=%s"
            tt1 = (self.d, self.b, self.c, date_time_string_y, date_time_string_m, date_time_string_d)
            cursor.execute(selectquery10,tt1)
            arecordss = cursor.fetchall()

            aal = []

            for rr in arecordss:
                if rr[3] == self.d and rr[4] == self.b and rr[5] == self.c and rr[6] == date_time_string_y and rr[
                    7] == date_time_string_m and rr[8] == date_time_string_d:
                    aal.append('1')
                    self.sa = len(aal)

            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
            cursor = self.conn.cursor()
            selectquery4 = "select * from student_infos where dept_id = %s and batch=%s"
            dept_ba1 = (self.a, self.b)
            cursor.execute(selectquery4,dept_ba1)
            records = cursor.fetchall()
            selectquery8 = "select * from student_attendances where dept=%s and batch=%s and course_no=%s and year=%s and month=%s and date=%s"
            tt2 = (self.d, self.b, self.c, date_time_string_y, date_time_string_m, date_time_string_d)
            cursor.execute(selectquery8,tt2)
            arecords = cursor.fetchall()
            # for rr1 in arecords:
            #     if rr1!='':
            #         self.allatten1.append(rr1[2]+','+rr1[1]+','+rr1[9])
            date_time_string1 = datetime.datetime.now().strftime("%y_%m_%d")
            date_time_string_d = datetime.datetime.now().strftime("%d")
            date_time_string_m = datetime.datetime.now().strftime("%b")
            date_time_string_y = datetime.datetime.now().strftime("%Y")
            date_time_string11 = datetime.datetime.now().strftime("%I:%M %p")
            studentAbsentList = []
            namel = []
            for row in records:
                self.all_depts = row[3]
                self.all_batch = row[4]
                sm = 0
                if self.all_depts == self.a and self.all_batch == self.b:

                    for rr in arecords:
                        if rr[5] == self.c and rr[6] == date_time_string_y and rr[7] == date_time_string_m and rr[
                            8] == date_time_string_d:
                            if row[2] != rr[2]:
                                sm = sm + 1
                    #print(sm, self.sl, self.sa)
                if sm == self.sa:

                    path = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '/' + self.d + '/' + self.b + '/' + self.c + '_absent' + '.csv'
                    with open(path, 'r+') as f:

                        StudentAbsentList = f.readlines()
                        for line5 in StudentAbsentList:
                            entry = line5.split(',')
                            namel.append(entry[0])
                        #print(namel)
                        ss = 'Absent'
                        # timeList.append(entry[0])
                        if row[2] not in namel:
                            f.writelines(f'\n{row[2]},{row[1]},{ss}')
                            # kk=[]
                            # kk.append(row[2])
                            # kk.append(row[1])
                            # kk.append('Absent')
                            kk = row[2] + ',' + row[1]+',Absent\n'
                            #print(kk)
                            #self.abs.append(ll)
                            self.allatten.append(kk)
                            #print(self.allatten)
                            #self.allatten.append()
                            #self.allatten.append()
                            # self.nam1.append(str(row[1]))
                            # self.idd1.append(str(row[2]))
                            # self.pre1.append('Absent')
                            #self.allatten.sort()
                            #kk.clear()
                            namel.clear()

            sst=  'Total Student: ' + str(self.sl)+','
            tat = '    Total Present: ' + str(self.sa)+','
            tabb = '    Total Absence: ' + str((self.sl - self.sa))+',' + '\n\n'
            head = 'ID,' + 'Name,' + 'P/A\n\n'
            self.header.append(head.upper())


            self.tatt.append(tat)
            self.tabs.append(tabb)
            self.ts.append(sst)



            attendance(self)
        def mark_attendance1(name,id):
            path = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '/' + self.d + '/' + self.b + '/' + self.c + '.csv'
            with open(path,'r+') as f:
                    StudentAttendanceList = f.readlines()
                    csv_reader = reader(f)
                    nameList = []
                    date_time_string = datetime.datetime.now().strftime("%I:%M %p")

                    timeList=[]



                    for line in StudentAttendanceList:

                        entry = line.split(',')
                        nameList.append(entry[0])

                        #timeList.append(entry[0])
                    if name not in nameList:
                        self.tableWidget.setRowCount(self.jj1)
                        self.ll_n.append(name)
                        self.ll_d.append(date_time_string)
                        sayn=name+' Clocked In at '+date_time_string
                        self.engine.say(sayn)
                        f.writelines(f'\n{name},{id},{date_time_string}')

                        #print(name,date_time_string)
                        det=str(self.k)+'. '+id+' '+name+' '+date_time_string+'\n'

                        et=id+','+name+',' +date_time_string+'\n'

                        self.allatten1.append(et)
                        #self.ada.append(da)

                        cc='Course No: '+self.c.upper()+','
                        dat='DATE : '+date_time_string_d+' '+date_time_string_m+' '+date_time_string_y+','+'\n'

                        self.nam.append(str(name))
                        self.idd.append(str(id))

                        self.pre.append(str(date_time_string))
                        self.cours.append(cc)
                        self.ddt.append(dat)

                        self.allatten1.sort()
                        #list widget Add attendance
                        for qw in range(0,self.jj1):
                            self.tableWidget.setItem(self.row2, 0, QTableWidgetItem(str(self.jj1)))
                            self.tableWidget.setItem(self.row2, 1, QTableWidgetItem(str(name)))
                            self.tableWidget.setItem(self.row2, 2, QTableWidgetItem(str(id)))
                            self.tableWidget.setItem(self.row2, 3, QTableWidgetItem(str(date_time_string)))
                            self.row2 = self.row2 + 1
                            self.jj1=self.jj1 + 1




                        self.k=self.k+1

                        #database
                        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
                        cursor = self.conn.cursor()
                        selectquery1 = "insert into student_attendances (name,s_id,dept,batch,course_no,year,month,date,time,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        inf=(name,id,self.d,self.b,self.c,date_time_string_y,date_time_string_m,date_time_string_d,date_time_string,1)
                        #print(inf)
                        cursor.execute(selectquery1,inf)
                        self.conn.commit()
                        print(cursor.rowcount,'record inserted');
                        absent(self)
                        # path = 'Student Attendance/' + date_time_string_y + '/' + date_time_string_m + '/' + date_time_string1 + '/' + self.d + '/' + self.b + '/' + self.c + '_absent' + '.csv'
                        # with open(path, 'a+') as f:
                        #     f.writelines('')







        imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_cur_frame = face_recognition.face_locations(imgS)
        encodes_cur_frame = face_recognition.face_encodings(imgS, faces_cur_frame)

        # count = 0
        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=.43)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)

            best_match_index = np.argmin(face_dis)

            if match[best_match_index]:
                #print(face_dis)
                name = class_names[best_match_index].upper()
                id = student_id[best_match_index]
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(frame, str(1-face_dis[best_match_index]), (x1 + 6, y2 + 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 155, 0), 1)
                mark_attendance1(name,id)
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
            image = self.face_rec_(image, encode_list, class_names, self.student_id)
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
            self.imgLabel5.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel5.setScaledContents(True)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())