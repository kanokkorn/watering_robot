import cv2
import os, time

cascade = cv2.CascadeClassifier('opencv/cascade.xml')
cv2.ocl.setUseOpenCL(True)
cap = cv2.VideoCapture(0)

while 1:
    
    ret, img = cap.read()
    img_rz = cv2.resize(img ,(0,0) , fx = 0.9 , fy = 0.9 )
    gray = cv2.cvtColor(img_rz, cv2.COLOR_BGR2GRAY)
    palm = cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in palm:
        
        cv2.rectangle(img_rz,(x, y),(x+w, y+h),(175, 244, 65), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img_rz[y:y+h, x:x+w]
        cv2.imshow('img', roi_color)
        img_us = cv2.resize(img_rz ,(0,0) , fx = 1.1 , fy = 1.1 )
        cv2.imshow('CV', img_us)
        k = cv2.waitKey(1) & 0xff
        
        if k == 20:
            break

if __name__ == "__main__":
    
    cap.release()
    cv2.destroyAllWindows()
    pass
    
