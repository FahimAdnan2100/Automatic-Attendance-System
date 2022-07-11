import numpy as np
import cv2 as cv
url = 'D:/cam/record\G52457351_1_20220322T180329Z_20220322T180335Z.mp4'
cap = cv.VideoCapture(	'rtsp://admin:HZQRBI@192.168.0.106/H264?ch=1&subtype=0')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()