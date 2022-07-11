import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from datetime import date
import json

# from PIL import ImageGrab
k = 0
import mysql.connector

#course_no = input("Enter course code: ")
#course_no = str(course_no)
conn = mysql.connector.connect(host="localhost", user="root", password="", database="face")
cursor = conn.cursor()
selectquery = "select * from infos"
cursor.execute(selectquery)
records = cursor.fetchall()

images = []
classNames = []
studentEmail = []
now = datetime.now()
date = now.strftime('%m:%d:%Y')
k = 0

for row in records:
    b = 'D:/xampp4.27/htdocs/Attendance_App/Laravel/Attendance_App/public/'
    s = row[10]
    print(s)
    s=(b+s)
    #s = s[7:]
    print(s)
    curImg = cv2.imread(s, 1)
    images.append(curImg)
    classNames.append(row[1])
    studentEmail.append(row[4])
    # print(images)
    # cv2.imshow('img',images[k])
    k = k + 1
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name, email, date):
    global k
    # print(email)
    # saveInfo = conn.cursor()

    select = "select * from infos"
    cursor.execute(select)
    record = cursor.fetchall()
    # check = "IF EXISTS (SELECT * FROM infos WHERE email = email)"
    # date='02:25:2022'
    date = '02:26:2022'
    # print(record)

    s = "insert into attendance_infos (sid,name,dept,level,term,course_code,date,time) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        global now
        date_name = date + ' ' + name
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        # print(myDataList)
        # print(course_no)
        print(nameList)
        if date_name not in nameList:

            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{date_name},{"course_no"},{dtString}')
            for row in record:
                if (row[4] == email):
                    b1 = (row[0], row[1], row[2], row[5], row[6], "course_no", date, dtString)

            cursor.execute(s, b1)
            conn.commit()


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # img = captureScreen()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            email = studentEmail[matchIndex]
            date = now.strftime('%m:%d:%Y')
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name, email, date)
        else:
            name = 'Unknown'
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) == ord('q'):
        break
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

cursor.close()
conn.close()