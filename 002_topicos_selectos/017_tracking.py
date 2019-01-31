# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 08:11:03 2019
Este esta pendiente
@author: DevTequilaUser
"""

import cv2 as cv
import numpy as np

cv.namedWindow("webcam")
vc = cv.VideoCapture(0);
kernel = np.ones((5,5),np.uint8)
color = {'rojo':157,'verde':126,'azul':10}
limite=100

while True:
    next,frame = vc.read()
    rangomax=np.array([color['rojo']+limite,color['verde']+limite,color['azul']+limite]) 
    rangomin=np.array([color['rojo']-limite,color['verde']-limite,color['azul']-limite]) 
    mascara = cv.inRange(frame,np.array([50, 255, 50]), np.array([0, 51, 0]))
    abertura = cv.morphologyEx(mascara,cv.MORPH_OPEN,kernel)
    x,y,w,h = cv.boundingRect(abertura)
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)    
    cv.imshow("webcam",frame)
    
    if cv.waitKey(50) >= 0:
        cv.imwrite("testfilename.jpg",frame) #save image
        break;
        
cv.destroyWindow("webcam")
vc.release()