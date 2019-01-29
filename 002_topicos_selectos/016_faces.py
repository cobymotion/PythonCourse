# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:55:09 2019

@author: DevTequilaUser
"""

import cv2
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty(): raise Exception("¿Está seguro que es la ruta correcta?")
 
video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            print("encontro un rostro")
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]            
        cv2.imshow('Video', frame)
    if cv2.waitKey(50) >= 0:
        cv2.imwrite("testfilename.jpg",frame) #save image
        break;
 
video.release()
cv2.destroyAllWindows()