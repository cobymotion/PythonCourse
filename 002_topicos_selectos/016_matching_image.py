# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:49:50 2019

@author: DevTequilaUser
"""

import cv2

template= cv2.imread('template.jpg',0)
w, h = template.shape[::-1]
cv2.namedWindow("webcam")
vc = cv2.VideoCapture(0);

while True:
    next,frame = vc.read() 
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gris,template,cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(frame,top_left, bottom_right, 255, 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'OpenCV',(top_left[0],top_left[1]-10), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow("webcam",frame)
    if cv2.waitKey(50) >= 0:
        cv2.imwrite("testfilename.jpg",frame) #save image
        break;
        
cv2.destroyWindow("webcam")
vc.release()