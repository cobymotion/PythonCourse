# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:27:15 2019

@author: DevTequilaUser
"""

import serial, time

arduino = serial.Serial("COM3", 9600)
opcion=-1
time.sleep(2)
while opcion!=0:        
    try:
        opcion = int(input('valor'))
    except:
        opcion=4    
    if opcion ==1: 
        arduino.write(b'1')
    elif opcion==2:
        arduino.write(b'2')
    elif opcion==3:
        arduino.write(b's')
    else:
        arduino.write(b'x')
arduino.close()