# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 08:13:13 2019

@author: BigBoss
"""

import serial, time, threading

def medir(x):
    try:
        while True:
            y = x.readline().decode('utf-8')
            #print(y.decode("ascii",end=""))
            print(y)
    except:
        pass


x = serial.Serial("COM8",9600)
time.sleep(2)
thread = threading.Thread(target = medir, args=(x,))
thread.start()
while True:
    r = input("r.- Rojo:\na.- Amarillo:\nv.- Verde:\n Elige una opcion: ")
    r = r.encode("utf-8")
    print(r)
    if r == b"x":
        break
    x.write(r)
x.close()

