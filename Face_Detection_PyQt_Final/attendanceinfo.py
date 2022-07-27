from logging import Manager

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt5.QtWidgets import QDialog,QMessageBox,QListWidget
from PyQt5.QtTextToSpeech import QTextToSpeech
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
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


class Ui_AttendanceDialog(QDialog):



    def __init__(self):
        super(Ui_AttendanceDialog, self).__init__()
        loadUi("./AttendanceMonth.ui", self)
        #self.engine = None

        #self.pushButton_3.clicked.connect(self.savefile)
        print('month')
        self.tableWidget.setColumnWidth(1,280)
        self.tableWidget.verticalHeader().setVisible(False)







    @pyqtSlot()
    def info(self, dd, bb, cc):
        self.d = dd
        self.b = bb
        self.c = cc
        print('dasdasd')
        path = 'Student Semester Attendance/' + self.d + '/' + self.b + '/' + self.c + '.csv'
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w+') as f:
                print('created')
                pass


        self.label_3.setText('COURSE         :     ' + self.c.upper())
        self.label_4.setText('Batch             :     ' + self.b.upper())
        self.label_5.setText('Department   :     ' + self.d.upper())

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
        cursor = self.conn.cursor()


        deptquery = "select * from depts"
        cursor.execute(deptquery)
        dept_records = cursor.fetchall()

        for dept_info in dept_records:
            if dept_info[1] == self.d:
                dept_id = dept_info[0]

        print(dept_id)


        totalsquery =  "select * from student_attendances where dept=%s and batch=%s and course_no=%s"
        tt2 = (self.d, self.b, self.c)
        cursor.execute(totalsquery, tt2)
        srecords = cursor.fetchall()

        aa=[]
        for i in srecords:
            aa.append(i[6]+i[7]+i[8])
        x = np.array(aa)
        total = np.unique(x)
        cc=0
        for j in total:
            cc=cc+1
        print('total:' ,cc)
        self.label_6.setText('Total Classes   :     ' + str(cc))

        selectquery = "select * from student_attendances where dept=%s and batch=%s and course_no=%s"
        tt2 = (self.d, self.b, self.c)
        cursor.execute(selectquery, tt2)
        records = cursor.fetchall()

        selectquery1 = "select * from student_infos where dept_id=%s and batch=%s "
        tt3 = (dept_id, self.b)
        cursor.execute(selectquery1, tt3)
        records_student = cursor.fetchall()
        count1 = 0;
        print(count1)



        k = open(path, 'r+')

        totalStudent=0
        for row_student in records_student:
            totalStudent = totalStudent+1

        k.writelines(f'\n Dept :{(self.d).upper()},Batch No :{(self.b)}, { (self.c).upper()},Total Students: {totalStudent},\n\n')

        k.writelines(f'\n Name ,  ID,Total, Percent(%),Number,\n')

        row1=0
        j=1

        for row_student in records_student:
            self.tableWidget.setRowCount(j)
            self.name =row_student[1]
            self.id = row_student[2]
            for row in records:

                if row_student[2] == row[2]:
                    #print(str(row_student[2]+"  "+str(row[2])))
                    count1=count1+1
                    #print(count1)
            infos = self.name+',           '+self.id+',          '+str(count1)+','
            #print('count: ',(count1*100)/42)
            percent = (count1*100)/cc
            print(percent)
            p1=round(percent)
            tnum = (15*p1)/100
            print('num:',tnum)
            t1=round(tnum)
            #self.tableWidget.addItem(self.name+',           '+self.id+',          '+str(count1)+',           '+str(p1)+',           '+str(t1))
            #k.writelines(infos)
            # inff = [{"name":self.name,"id":self.id,"total":str(count1),"percent":str(p1),"number":str(t1)}]
            # print(inff)
            self.tableWidget.setItem(row1, 0, QTableWidgetItem(str(row1+1)))
            self.tableWidget.setItem(row1, 1, QTableWidgetItem(self.name))
            self.tableWidget.setItem(row1, 2, QTableWidgetItem(self.id))
            self.tableWidget.setItem(row1, 3, QTableWidgetItem(str(count1)))
            self.tableWidget.setItem(row1, 4, QTableWidgetItem(str(p1)+'%'))
            self.tableWidget.setItem(row1, 5, QTableWidgetItem(str(t1)))

            row1=row1+1
            k.writelines(f'\n{self.name},{self.id},{str(count1)},{str(p1)}%,{str(t1)}')
            count1=0
            j=j+1





        self.pushButton_2.clicked.connect(self.runSlot6)

    def runSlot6(self):
        print("Clicked Run")


        self.outputWindow3_()  # Create and open new output window
        self.close()
        # self.out()

    def outputWindow3_(self):
        from student import Ui_StudentDialog
        self._new_window = Ui_StudentDialog()
        self._new_window.show()


        print("Video Played")


    # def savefile(self):
    #     path = 'Student Semester Attendance /' + self.d + '/' + self.b + '/' + self.b  + '_attendance' + '.csv'
    #     if not os.path.exists(path):
    #         os.makedirs(os.path.dirname(path), exist_ok=True)
    #         with open(path, 'w+') as f:
    #             pass
    #
    #     k = open(path, 'r+')
    #     k.writelines(self.cours)




