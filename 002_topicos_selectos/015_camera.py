# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:03:41 2019

@author: DevTequilaUser
"""

from cv2 import *

namedWindow("webcam")
vc = VideoCapture(0);

while True:
    next,frame = vc.read()
    
    imshow("webcam",frame)
    
    if waitKey(50) >= 0:
        imwrite("testfilename.jpg",frame) #save image
        break;
        
destroyWindow("webcam")
vc.release()