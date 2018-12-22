import numpy as np
#from numba import jit # remove if not use
import cv2
import os, time

face_cascade = cv2.CascadeClassifier('C:\\Users\\GEFORCE\\Documents\\watering_robot\\opencv\\stage5.xml')
#eye_cascade = cv2.CascadeClassifier('C:\\Users\GEFORCE\\Documents\\ani_face_dct.xml')
cv2.ocl.setUseOpenCL(True)
cap = cv2.VideoCapture(0)
#C:\\Users\\GEFORCE\\Documents\\test_vid\\Gochumon_OP.mp4 # video location 
#num = 0
while 1:
    ret, img = cap.read()
    img_rz = cv2.resize(img ,(0,0) , fx = 0.9 , fy = 0.9 )
    gray = cv2.cvtColor(img_rz, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img_rz,(x, y),(x+w, y+h),(175, 244, 65), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img_rz[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #cv2.putText(img,"found", (x,y), cv2.FONT_HERSHEY_DUPLEX, 1,(244, 66, 167))
        #for (ex, ey, ew, eh) in eyes:
        #    cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh),(146, 66, 244), 2)
        #cv2.imwrite('C:\\Users\\GEFORCE\\Documents\\cv_img_gochuumon_op2\\cv_cap_img'+str(num)+'.jpg', roi_color) #save img to folder
        #print('found')
        cv2.imshow('img', roi_color)
        #num = num+1
        img_us = cv2.resize(img_rz ,(0,0) , fx = 1.1 , fy = 1.1 )
        cv2.imshow('CV', img_us)
        k = cv2.waitKey(1) & 0xff
        if k == 20:
            break
#@jit  #remove if not use
def ani_cv(cap):
    cap.release()
    cv2.destroyAllWindows()
    return
