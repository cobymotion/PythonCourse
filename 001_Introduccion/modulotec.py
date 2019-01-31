# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:46:05 2019

@author: DevTequilaUser
"""

import datetime

def calculonomina(fecha):
    mes = fecha.month
    year = fecha.year
    if fecha.day>15:    
        if mes==12:
            mes = 1; 
            year+=1
        else:
            mes+=1
        quincena = datetime.date(year,mes,1)
        quincena = quincena - datetime.timedelta(days=1)
    else:
        quincena = datetime.date(year,mes,15)

    falta  = quincena - fecha

    print("Falta para que paguen ", falta.days )
    print("Fecha estimada del pago es ", quincena)
    

def ingresos(*ingresos):
    suma = 0
    for ingreso in ingresos:
        suma+=ingreso
    return suma