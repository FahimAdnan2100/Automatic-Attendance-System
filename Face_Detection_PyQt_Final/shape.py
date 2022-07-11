import cv2
import numpy as np

img = cv2.imread('shapes.png')
original = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

ROI_number = 0
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for cnt in cnts:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print(len(approx))
    if len(approx)==5:
        print("Blue = pentagon")
        cv2.drawContours(img,[cnt],0,255,-1)
        cv2.putText(img,'pentagon',)
    elif len(approx)==3:
        print("Green = triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print("Red = square")
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 6:
        print("Cyan = Hexa")
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) == 8:
        print("White = Octa")
        cv2.drawContours(img,[cnt],0,(255,255,255),-1)
    elif len(approx) > 12:
        print("Yellow = circle")
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)

cv2.imshow('image', img)
cv2.imshow('Binary',thresh)
cv2.waitKey()