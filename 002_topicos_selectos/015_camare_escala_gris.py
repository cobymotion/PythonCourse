# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:40:55 2019

@author: DevTequilaUser
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:03:41 2019

@author: DevTequilaUser
"""

import cv2

cv2.namedWindow("webcam")
vc = cv2.VideoCapture(0);

while True:
    next,frame = vc.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("webcam",gris)
    
    if cv2.waitKey(50) >= 0:
        cv2.imwrite("testfilename.jpg",gris) #save image
        break;
        
cv2.destroyWindow("webcam")
vc.release()