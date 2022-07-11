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
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
faceCascade = cv2.CascadeClassifier(
    '../../../../D:/xampp4.27/htdocs/Attendance_App/Laravel/Attendance_App/public/upload/opencv-master/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

detector = cv2.CascadeClassifier(
    "../../../../D:/xampp4.27/htdocs/Attendance_App/Laravel/Attendance_App/public/upload/opencv-master/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml");
#course_no = input("Enter course code: ")
#course_no = str(course_no)
course_no='cse-4000'
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
    s = str(row[10])
    s = s[7:]
    # print(s)
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
        img_numpy = np.array(img, 'uint8')

        faces = detector.detectMultiScale(img_numpy);
        for (x, y, w, h) in faces:
            encodeList.append(img_numpy[y:y + h, x:x + w])
    return encodeList


faces = findEncodings(images)
recognizer.train(faces)
# Save the model into trainer/trainer.yml
recognizer.write('trainer.yml')  # recognizer.save() worked on Mac, but not on Pi


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
    with open('cse-4000' + '.csv', 'r+') as f:
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
            f.writelines(f'\n{date_name},{course_no},{dtString}')
            for row in record:
                if (row[4] == email):
                    b1 = (row[0], row[1], row[2], row[5], row[6], course_no, date, dtString)

            cursor.execute(s, b1)
            conn.commit()


encodeListKnown = findEncodings(images)
print('Encoding Complete')
recognizer.read('D:/xampp4.27/htdocs/Attendance_App/Laravel/Attendance_App/public/upload/trainer.yml')
cascadePath = cv2.CascadeClassifier(
    'D:/xampp4.27/htdocs/Attendance_App/Laravel/Attendance_App/public/upload/opencv-master/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture("rtsp://admin:HZQRBI@192.168.0.106")
cap.set(3, 640)  # set video widht
cap.set(4, 480)  # set video height
cap.set(cv2.CAP_PROP_FPS, 15)
# Define min window size to be recognized as a face
minW = 0.1 * cap.get(3)
minH = 0.1 * cap.get(4)
# Percentage
in_min = 0
in_max = 100
out_min = 100
out_max = 0
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # img = captureScreen()
    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faces = faceCascade.detectMultiScale(
        imgS,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        confidence = recognizer.predict(imgS[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):

            con_data = round(confidence)
            print(" Confidence: " + str(con_data) + "%")
            # confidence = "  {0}%".format(round(100 - confidence))


        else:

            con_data = round(confidence)
            # confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(1), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        # cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        cv2.putText(img, str(con_data), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        # con_confidence = (confidence - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    cv2.imshow('Webcam', img)

    if cv2.waitKey(30) == ord('q'):
        break
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

cursor.close()
conn.close()