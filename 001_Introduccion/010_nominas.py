# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 02:24:47 2019

@author: coby_
Practica 10: uso de librerias 
"""

import datetime 

hoy = datetime.date.today(); 
mes = hoy.month
year = hoy.year
if hoy.day>15:    
    if mes==12:
        mes = 1; 
        year+=1
    else:
        mes+=1
    quincena = datetime.date(year,mes,1)
    quincena = quincena - datetime.timedelta(days=1)
else:
    quincena = datetime.date(year,mes,15)

falta  = quincena - hoy

print("Falta para que paguen ", falta.days )
print("Fecha estimada del pago es ", quincena)
    

